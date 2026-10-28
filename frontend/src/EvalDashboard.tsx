import { useEffect, useMemo, useState } from "react";
import "./EvalDashboard.css";

type BotKey = "rag" | "okf" | "mixed";

type BotSummary = {
  n: number;
  pass_rate: number;
  avg_overall: number;
  avg_correctness: number;
  avg_groundedness: number;
  avg_completeness: number;
  avg_retrieve_ms: number;
  p50_retrieve_ms: number;
  wrong_refuse: number;
  avg_context_tokens_est: number;
  avg_answer_tokens_est: number;
};

type Failure = {
  id: string;
  bot: BotKey;
  category: string;
  question: string;
  overall: number;
  correctness: number;
  completeness: number;
  reason: string;
  retrieve_latency_ms: number | null;
};

type DashboardData = {
  meta: {
    title: string;
    n_questions: number;
    generator: string;
    gold: string;
    judge: string;
    pass_rule: string;
    verdict: string;
    winner: BotKey;
  };
  summary: Record<BotKey, BotSummary>;
  wins: Record<BotKey, number>;
  ties: number;
  fail_count: number;
  category: Record<string, Record<BotKey, { pass_rate: number; n: number }>>;
  failures: Failure[];
};

const BOTS: { id: BotKey; label: string; blurb: string }[] = [
  { id: "rag", label: "RAG", blurb: "Dense vectors over doc chunks" },
  { id: "okf", label: "OKF", blurb: "BM25 + concept link graph" },
  { id: "mixed", label: "Mixed", blurb: "RRF fusion of both" },
];

const CATEGORY_ORDER = [
  "definition",
  "query_framing",
  "platform",
  "navigation",
  "features",
  "search",
  "export",
  "basketball",
  "edge",
];

function pct(n: number) {
  return `${Math.round(n * 100)}%`;
}

function heatClass(rate: number) {
  if (rate >= 0.9) return "heat-hi";
  if (rate >= 0.7) return "heat-mid";
  if (rate >= 0.5) return "heat-low";
  return "heat-bad";
}

function labelCat(c: string) {
  return c.replace(/_/g, " ");
}

export default function EvalDashboard() {
  const [data, setData] = useState<DashboardData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [failBot, setFailBot] = useState<BotKey | "all">("all");
  const [selectedFail, setSelectedFail] = useState<Failure | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetch("/evals/dashboard.json")
      .then(async (res) => {
        if (!res.ok) throw new Error(`Failed to load dashboard (${res.status})`);
        return res.json() as Promise<DashboardData>;
      })
      .then((json) => {
        if (!cancelled) setData(json);
      })
      .catch((err: unknown) => {
        if (!cancelled) setError(err instanceof Error ? err.message : "Load failed");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  const filteredFails = useMemo(() => {
    if (!data) return [];
    return failBot === "all" ? data.failures : data.failures.filter((f) => f.bot === failBot);
  }, [data, failBot]);

  if (error) {
    return (
      <div className="dash-shell">
        <p className="dash-error">{error}</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="dash-shell">
        <p className="dash-loading">Loading benchmark…</p>
      </div>
    );
  }

  const winner = data.meta.winner;
  const maxPass = Math.max(...BOTS.map((b) => data.summary[b.id].pass_rate));
  const maxLatency = Math.max(...BOTS.map((b) => data.summary[b.id].avg_retrieve_ms));

  return (
    <div className="dash-shell">
      <header className="dash-hero">
        <div>
          <p className="dash-kicker">Benchmark</p>
          <h2 className="dash-title">{data.meta.title}</h2>
          <p className="dash-verdict">{data.meta.verdict}</p>
        </div>
        <div className="dash-meta-chips">
          <span>{data.meta.n_questions} questions</span>
          <span>Gold · {data.meta.gold}</span>
          <span>Judge · {data.meta.judge}</span>
          <span>Pass · {data.meta.pass_rule}</span>
        </div>
      </header>

      <section className="kpi-grid" aria-label="Strategy comparison">
        {BOTS.map((b) => {
          const s = data.summary[b.id];
          const isWinner = b.id === winner;
          return (
            <article key={b.id} className={`kpi-card${isWinner ? " winner" : ""}`}>
              <div className="kpi-top">
                <h3>{b.label}</h3>
                {isWinner ? <span className="winner-pill">Best quality</span> : null}
              </div>
              <p className="kpi-blurb">{b.blurb}</p>
              <p className="kpi-pass">{pct(s.pass_rate)}</p>
              <p className="kpi-pass-label">pass rate</p>
              <dl className="kpi-stats">
                <div>
                  <dt>Overall</dt>
                  <dd>{s.avg_overall.toFixed(2)} / 5</dd>
                </div>
                <div>
                  <dt>Retrieve</dt>
                  <dd>{Math.round(s.avg_retrieve_ms)} ms</dd>
                </div>
                <div>
                  <dt>Wrong refuse</dt>
                  <dd>{s.wrong_refuse}</dd>
                </div>
                <div>
                  <dt>Solo wins</dt>
                  <dd>{data.wins[b.id]}</dd>
                </div>
              </dl>
            </article>
          );
        })}
      </section>

      <section className="dash-panels">
        <article className="dash-panel">
          <h3>Pass rate</h3>
          <p className="panel-note">Share of answers with judge overall ≥ 4</p>
          <ul className="bar-list">
            {BOTS.map((b) => {
              const rate = data.summary[b.id].pass_rate;
              return (
                <li key={b.id}>
                  <div className="bar-label">
                    <span>{b.label}</span>
                    <strong>{pct(rate)}</strong>
                  </div>
                  <div className="bar-track" aria-hidden>
                    <div
                      className={`bar-fill bot-${b.id}`}
                      style={{ width: `${(rate / maxPass) * 100}%` }}
                    />
                  </div>
                </li>
              );
            })}
          </ul>
        </article>

        <article className="dash-panel">
          <h3>Retrieve latency</h3>
          <p className="panel-note">Average time to fetch context (no generation)</p>
          <ul className="bar-list">
            {BOTS.map((b) => {
              const ms = data.summary[b.id].avg_retrieve_ms;
              return (
                <li key={b.id}>
                  <div className="bar-label">
                    <span>{b.label}</span>
                    <strong>{Math.round(ms)} ms</strong>
                  </div>
                  <div className="bar-track" aria-hidden>
                    <div
                      className={`bar-fill muted bot-${b.id}`}
                      style={{ width: `${(ms / maxLatency) * 100}%` }}
                    />
                  </div>
                </li>
              );
            })}
          </ul>
        </article>
      </section>

      <section className="dash-panel dash-panel-wide">
        <h3>Pass rate by question type</h3>
        <p className="panel-note">Where each strategy holds up — darker green is stronger</p>
        <div className="heat-wrap">
          <table className="heat-table">
            <thead>
              <tr>
                <th>Category</th>
                {BOTS.map((b) => (
                  <th key={b.id}>{b.label}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {CATEGORY_ORDER.filter((c) => data.category[c]).map((cat) => (
                <tr key={cat}>
                  <th scope="row">{labelCat(cat)}</th>
                  {BOTS.map((b) => {
                    const cell = data.category[cat][b.id];
                    return (
                      <td key={b.id}>
                        <span className={`heat-cell ${heatClass(cell.pass_rate)}`}>
                          {pct(cell.pass_rate)}
                          <small>n={cell.n}</small>
                        </span>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <section className="dash-panel dash-panel-wide">
        <div className="fail-head">
          <div>
            <h3>Failure explorer</h3>
            <p className="panel-note">
              {data.fail_count} failed judgments · mostly OKF over-refusal on guides / platform docs
            </p>
          </div>
          <div className="fail-filters" role="tablist" aria-label="Filter failures by bot">
            {(["all", "rag", "okf", "mixed"] as const).map((id) => (
              <button
                key={id}
                type="button"
                role="tab"
                aria-selected={failBot === id}
                className={`fail-tab${failBot === id ? " active" : ""}`}
                onClick={() => {
                  setFailBot(id);
                  setSelectedFail(null);
                }}
              >
                {id === "all" ? "All" : id.toUpperCase()}
              </button>
            ))}
          </div>
        </div>

        <div className="fail-layout">
          <ul className="fail-list">
            {filteredFails.map((f) => (
              <li key={`${f.id}-${f.bot}`}>
                <button
                  type="button"
                  className={`fail-row${selectedFail?.id === f.id && selectedFail.bot === f.bot ? " active" : ""}`}
                  onClick={() => setSelectedFail(f)}
                >
                  <span className={`bot-tag bot-${f.bot}`}>{f.bot}</span>
                  <span className="fail-q">{f.question}</span>
                  <span className="fail-score">{f.overall}/5</span>
                </button>
              </li>
            ))}
            {filteredFails.length === 0 ? <li className="fail-empty">No failures for this filter.</li> : null}
          </ul>

          <aside className="fail-detail">
            {selectedFail ? (
              <>
                <p className="fail-detail-id">
                  {selectedFail.id} · {labelCat(selectedFail.category)} · {selectedFail.bot.toUpperCase()}
                </p>
                <h4>{selectedFail.question}</h4>
                <dl className="fail-scores">
                  <div>
                    <dt>Overall</dt>
                    <dd>{selectedFail.overall}</dd>
                  </div>
                  <div>
                    <dt>Correct</dt>
                    <dd>{selectedFail.correctness}</dd>
                  </div>
                  <div>
                    <dt>Complete</dt>
                    <dd>{selectedFail.completeness}</dd>
                  </div>
                </dl>
                <p className="fail-reason">{selectedFail.reason}</p>
              </>
            ) : (
              <p className="fail-placeholder">Select a failure to read the judge’s reason.</p>
            )}
          </aside>
        </div>
      </section>

      <footer className="dash-foot">
        <p>
          Method: retrieve with each strategy → generate from that context only → score vs gold.
          Ties on overall: {data.ties}. Generator: {data.meta.generator}.
        </p>
      </footer>
    </div>
  );
}
