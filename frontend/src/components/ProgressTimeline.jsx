// components/ProgressTimeline.jsx

import { CheckCircle2, Circle, LoaderCircle } from "lucide-react";

const STEPS = [
  { node: "validator", label: "Verify company identity" },
  { node: "research", label: "Collect public information" },
  { node: "evidence", label: "Synthesize evidence" },
  { node: "overview", label: "Generate company overview" },
  { node: "business", label: "Analyze business model" },
  { node: "challenges", label: "Identify business challenges" },
  { node: "ai_opportunities", label: "Generate AI opportunities" },
  { node: "ceo_pitch", label: "Prepare CEO pitch" },
  { node: "report", label: "Finalize report" },
];

export default function ProgressTimeline({ progress, loading }) {
  const completed = progress.filter((e) => e.type === "completed").map((e) => e.node);
  const activeIndex = completed.length;
  const isIdle = !loading && completed.length === 0;
  const isDone = completed.length === STEPS.length;

  const status = isDone ? "Complete" : loading ? "In progress" : "Standby";
  const statusColor = isDone ? "text-signal" : loading ? "text-marker" : "text-fg-faint";

  return (
    <div className="rounded-2xl border border-line bg-surface p-6">
      <div className="mb-6 flex items-center justify-between border-b border-line pb-4">
        <div>
          <span className="font-mono text-xs tracking-widest text-fg-faint">FIELD LOG</span>
          <h2 className="mt-1 font-display text-lg font-medium text-fg">Research progress</h2>
        </div>
        <span className={`font-mono text-xs ${statusColor}`}>{status}</span>
      </div>

      {isIdle ? (
        <p className="font-mono text-sm text-fg-faint">
          awaiting company name
          <span className="animate-blink-cursor ml-1">▍</span>
        </p>
      ) : (
        <div className="space-y-4">
          {STEPS.map((step, index) => {
            const isCompleted = completed.includes(step.node);
            const isActive = loading && !isCompleted && index === activeIndex;

            const code = String(index + 1).padStart(2, "0");

            return (
              <div key={step.node} className="flex items-center gap-3">
                <span
                  className={`font-mono text-[10px] w-6 shrink-0 ${
                    isCompleted ? "text-signal" : isActive ? "text-marker" : "text-fg-faint"
                  }`}
                >
                  {code}
                </span>

                <span className="relative flex h-5 w-5 shrink-0 items-center justify-center">
                  {isCompleted ? (
                    <CheckCircle2 size={18} className="text-signal" />
                  ) : isActive ? (
                    <>
                      <span className="absolute h-2 w-2 rounded-full bg-marker animate-pulse-ring" />
                      <LoaderCircle size={18} className="animate-spin text-marker" />
                    </>
                  ) : (
                    <Circle size={18} className="text-line-strong" />
                  )}
                </span>

                <span
                  className={`text-sm ${
                    isCompleted ? "text-fg" : isActive ? "text-fg" : "text-fg-faint"
                  }`}
                >
                  {step.label}
                </span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}




