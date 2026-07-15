// pages/ResearchPage.jsx

import { useState } from "react";
import SearchBar from "../components/SearchBar";
import ProgressTimeline from "../components/ProgressTimeline";
import ReportViewer from "../components/ReportViewer";

export default function ResearchPage() {
  const [progress, setProgress] = useState([]);
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-ink text-fg">
      <div className="mx-auto max-w-7xl px-8 py-16">
        <div className="text-center">
          <span className="font-mono text-xs uppercase tracking-[0.3em] text-fg-faint">
            AI research desk
          </span>
          <h1 className="mt-4 font-display text-5xl font-medium tracking-tight text-fg">
            Company Research Agent
          </h1>
          <p className="mt-4 text-fg-muted">
            Point it at a company. It builds the dossier.
          </p>
        </div>

        <div className="mt-10">
          <SearchBar
            loading={loading}
            setLoading={setLoading}
            setProgress={setProgress}
            setReport={setReport}
          />
        </div>

        <div className="mt-12 grid grid-cols-12 gap-6">
          <div className="col-span-4">
            <div className="sticky top-8">
              <ProgressTimeline progress={progress} loading={loading} />
            </div>
          </div>

          <div className="col-span-8">
            <ReportViewer report={report} />
          </div>
        </div>
      </div>
    </div>
  );
}



