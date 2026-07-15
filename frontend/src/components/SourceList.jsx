// components/SourceList.jsx

import { ExternalLink } from "lucide-react";

export default function SourceList({ citations = [] }) {
  if (!citations.length) {
    return <p className="text-sm text-fg-faint">No sources available.</p>;
  }

  return (
    <div className="space-y-3">
      {citations.map((source, index) => (
        <a
          key={index}
          href={source.url}
          target="_blank"
          rel="noopener noreferrer"
          className="group flex items-start justify-between gap-4 rounded-xl border border-line bg-surface-2 p-4 transition-colors duration-150 hover:border-marker/50"
        >
          <div className="flex min-w-0 items-start gap-3">
            <span className="mt-0.5 shrink-0 font-mono text-xs text-fg-faint">
              {String(index + 1).padStart(2, "0")}
            </span>
            <div className="min-w-0">
              <h3 className="truncate text-sm font-medium text-fg transition-colors group-hover:text-marker">
                {source.title}
              </h3>
              <p className="mt-1.5 truncate font-mono text-xs text-fg-faint">
                {source.url}
              </p>
            </div>
          </div>
          <ExternalLink
            size={15}
            className="mt-0.5 shrink-0 text-fg-faint transition-colors group-hover:text-marker"
          />
        </a>
      ))}
    </div>
  );
}



