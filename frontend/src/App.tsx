import { FormEvent, KeyboardEvent, useEffect, useRef, useState } from "react";
import { askBotStream, BotName, Citation } from "./api";
import "./App.css";

type Message = {
  id: string;
  role: "user" | "bot";
  text: string;
  bot?: BotName;
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

const BOTS: { id: BotName; label: string; hint: string }[] = [
  { id: "rag", label: "RAG", hint: "Dense vector chunks (Qdrant)" },
  { id: "okf", label: "OKF", hint: "BM25 + knowledge graph" },
  { id: "mixed", label: "Mixed", hint: "RRF fuse of RAG + OKF" },
];

function uid() {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
}

function botLabel(bot?: BotName) {
  return BOTS.find((b) => b.id === bot)?.label ?? "RAG";
}

export default function App() {
  const [bot, setBot] = useState<BotName>("rag");
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "welcome",
      role: "bot",
      text: "Hi — ask me about Athlyte Search. Switch RAG / OKF / Mixed above to compare retrieval strategies.",
      grounded: true,
      bot: "rag",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const activeHint = BOTS.find((b) => b.id === bot)?.hint ?? "";

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function send(question: string) {
    const trimmed = question.trim();
    if (!trimmed || loading) return;

    const botId = uid();
    const selectedBot = bot;
    setInput("");
    setMessages((prev) => [
      ...prev,
      { id: uid(), role: "user", text: trimmed },
      {
        id: botId,
        role: "bot",
        text: "",
        bot: selectedBot,
        streaming: true,
        grounded: true,
        citations: [],
      },
    ]);
    setLoading(true);

    try {
      await askBotStream(
        trimmed,
        {
          onMeta: ({ bot: metaBot, intent, citations, grounded }) => {
            setMessages((prev) =>
              prev.map((m) =>
                m.id === botId
                  ? { ...m, bot: metaBot, intent, citations, grounded }
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
        },
        selectedBot,
      );
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
          Quick help for stats, searches, dashboards — compare RAG, OKF, and Mixed retrieval.
        </p>

        <div className="bot-switcher" role="tablist" aria-label="Retrieval strategy">
          {BOTS.map((b) => (
            <button
              key={b.id}
              type="button"
              role="tab"
              aria-selected={bot === b.id}
              className={`bot-tab${bot === b.id ? " active" : ""}`}
              onClick={() => setBot(b.id)}
              disabled={loading}
            >
              {b.label}
            </button>
          ))}
        </div>
        <p className="bot-hint">{activeHint}</p>
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
                {msg.role === "bot" && msg.bot ? (
                  <span className={`bot-badge bot-${msg.bot}`}>{botLabel(msg.bot)}</span>
                ) : null}
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
            placeholder={`Ask with ${botLabel(bot)}…`}
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
