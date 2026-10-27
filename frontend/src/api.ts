export type Citation = {
  source: string;
  section: string;
  snippet: string;
};

export type ChatResponse = {
  answer: string;
  intent: string;
  citations: Citation[];
  grounded: boolean;
};

export type StreamHandlers = {
  onMeta?: (meta: { intent: string; citations: Citation[]; grounded: boolean }) => void;
  onToken?: (text: string) => void;
  onDone?: (info: { grounded: boolean; total_ms?: number }) => void;
  onError?: (message: string) => void;
};

const API_BASE = import.meta.env.VITE_API_BASE ?? "";

export async function askBot(question: string): Promise<ChatResponse> {
  const res = await fetch(`${API_BASE}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  if (!res.ok) {
    let detail = `Request failed (${res.status})`;
    try {
      const body = await res.json();
      if (typeof body?.detail === "string") detail = body.detail;
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }

  return res.json();
}

export async function askBotStream(question: string, handlers: StreamHandlers): Promise<void> {
  const res = await fetch(`${API_BASE}/api/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "text/event-stream" },
    body: JSON.stringify({ question }),
  });

  if (!res.ok || !res.body) {
    let detail = `Request failed (${res.status})`;
    try {
      const body = await res.json();
      if (typeof body?.detail === "string") detail = body.detail;
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });

    const parts = buffer.split("\n\n");
    buffer = parts.pop() ?? "";

    for (const part of parts) {
      const line = part
        .split("\n")
        .map((l) => l.trim())
        .find((l) => l.startsWith("data:"));
      if (!line) continue;
      const raw = line.slice(5).trim();
      if (!raw) continue;

      let event: {
        type: string;
        intent?: string;
        citations?: Citation[];
        grounded?: boolean;
        text?: string;
        message?: string;
        total_ms?: number;
      };
      try {
        event = JSON.parse(raw);
      } catch {
        continue;
      }

      if (event.type === "meta") {
        handlers.onMeta?.({
          intent: event.intent ?? "general",
          citations: event.citations ?? [],
          grounded: Boolean(event.grounded),
        });
      } else if (event.type === "token" && event.text) {
        handlers.onToken?.(event.text);
      } else if (event.type === "done") {
        handlers.onDone?.({
          grounded: Boolean(event.grounded),
          total_ms: event.total_ms,
        });
      } else if (event.type === "error") {
        handlers.onError?.(event.message || "Stream failed");
      }
    }
  }
}
