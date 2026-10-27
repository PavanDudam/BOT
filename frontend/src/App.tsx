import { FormEvent, KeyboardEvent, useEffect, useRef, useState } from "react";
import { askBotStream, Citation } from "./api";
import "./App.css";

type Message = {
  id: string;
  role: "user" | "bot";
  text: string;
  intent?: string;
  grounded?: boolean;
  citations?: Citation[];
  error?: boolean;
  streaming?: boolean;
};

const SUGGESTIONS = [
  "What is rushing yards?",
  "How to frame query using rushing yards",
  "How do I open the Team Dashboard?",
  "What sports does Athlyte Search support?",
];

function uid() {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
}

export default function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "bot",
      text: "Hi — ask me about Athlyte Search. Definitions, how to write a search, dashboards, navigation, exports… I’m here to help.",
      grounded: true,
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function send(question: string) {
    const trimmed = question.trim();
    if (!trimmed || loading) return;

    const botId = uid();
    setInput("");
    setMessages((prev) => [
      ...prev,
      { id: uid(), role: "user", text: trimmed },
      {
        id: botId,
        role: "bot",
        text: "",
        streaming: true,
        grounded: true,
        citations: [],
      },
    ]);
    setLoading(true);

    try {
      await askBotStream(trimmed, {
        onMeta: ({ intent, citations, grounded }) => {
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botId
                ? { ...m, intent, citations, grounded }
                : m,
            ),
          );
        },
        onToken: (text) => {
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botId ? { ...m, text: m.text + text } : m,
            ),
          );
        },
        onDone: ({ grounded }) => {
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botId
                ? {
                    ...m,
                    streaming: false,
                    grounded,
                    text:
                      m.text ||
                      "Hmm, I didn’t get a clear answer there. Want to try asking another way?",
                  }
                : m,
            ),
          );
        },
        onError: (message) => {
          setMessages((prev) =>
            prev.map((m) =>
              m.id === botId
                ? { ...m, text: message, error: true, streaming: false, grounded: false }
                : m,
            ),
          );
        },
      });
    } catch (err) {
      const message = err instanceof Error ? err.message : "Something went wrong.";
      setMessages((prev) =>
        prev.map((m) =>
          m.id === botId
            ? { ...m, text: message, error: true, streaming: false, grounded: false }
            : m,
        ),
      );
    } finally {
      setLoading(false);
      inputRef.current?.focus();
    }
  }

  function onSubmit(e: FormEvent) {
    e.preventDefault();
    void send(input);
  }

  function onKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      void send(input);
    }
  }

  return (
    <div className="shell">
      <div className="glow" aria-hidden />
      <header className="hero">
        <p className="brand">Athlyte Search</p>
        <h1>Platform Help</h1>
        <p className="tagline">
          Quick help for stats, searches, dashboards, and getting around the product.
        </p>
      </header>

      <main className="panel">
        <div className="thread" role="log" aria-live="polite">
          {messages.map((msg) => (
            <article
              key={msg.id}
              className={`bubble ${msg.role}${msg.error ? " error" : ""}${msg.streaming ? " streaming" : ""}`}
            >
              <div className="meta">
                <span>{msg.role === "user" ? "You" : "Athlyte Help"}</span>
              </div>
              <div className="body">
                {msg.text || (msg.streaming ? "…" : "")}
                {msg.streaming ? <span className="cursor" aria-hidden /> : null}
              </div>
            </article>
          ))}
          <div ref={bottomRef} />
        </div>

        <div className="suggestions">
          {SUGGESTIONS.map((s) => (
            <button key={s} type="button" className="suggestion" onClick={() => void send(s)} disabled={loading}>
              {s}
            </button>
          ))}
        </div>

        <form className="composer" onSubmit={onSubmit}>
          <textarea
            ref={inputRef}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={onKeyDown}
            placeholder="Ask about Athlyte Search…"
            rows={2}
            disabled={loading}
          />
          <button type="submit" className="send" disabled={loading || !input.trim()}>
            Ask
          </button>
        </form>
      </main>
    </div>
  );
}
