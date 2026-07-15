// components/SearchBar.jsx

import { useState } from "react";
import { LoaderCircle, ArrowRight } from "lucide-react";
import { researchCompany } from "../services/api";

export default function SearchBar({ loading, setLoading, setProgress, setReport }) {
  const [company, setCompany] = useState("");
  const [focused, setFocused] = useState(false);

  const handleResearch = async () => {
    if (!company.trim() || loading) return;

    setLoading(true);
    setProgress([]);
    setReport(null);

    try {
      await researchCompany(company, (event) => {
        if (event.type === "completed") {
          setProgress((prev) => [...prev, event]);
        }
        if (event.type === "complete") {
          setReport(event.report);
        }
      });
    } catch (error) {
      console.error(error);
      setProgress([{ type: "error", message: "Something went wrong." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-auto max-w-2xl">
      <label className="mb-3 block font-mono text-[11px] uppercase tracking-[0.2em] text-fg-faint">
        Research target
      </label>

      <div
        className={`flex items-center gap-3 rounded-xl border bg-surface px-4 py-3.5 transition-all duration-200 ${
          focused ? "border-marker/60 shadow-[0_0_0_3px_rgba(217,164,65,0.12)]" : "border-line"
        }`}
      >
        <span className="font-mono text-base text-marker">›</span>

        <input
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          onKeyDown={(e) => e.key === "Enter" && handleResearch()}
          placeholder="e.g. Stripe, Anthropic, Shopify..."
          className="flex-1 bg-transparent text-[15px] text-fg outline-none placeholder:text-fg-faint"
        />

        <button
          onClick={handleResearch}
          disabled={loading}
          className="group flex items-center gap-2 rounded-lg bg-marker px-4 py-2.5 text-sm font-medium text-ink transition disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? (
            <LoaderCircle className="animate-spin" size={16} />
          ) : (
            <>
              Run research
              <ArrowRight size={15} className="transition-transform group-hover:translate-x-0.5" />
            </>
          )}
        </button>
      </div>

      <p className="mt-2.5 font-mono text-[11px] text-fg-faint">
        Press Enter — cross-references filings, press coverage, and public technical footprint.
      </p>
    </div>
  );
}



