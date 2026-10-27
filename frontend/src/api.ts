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
