// // components/EmptyState.jsx


// import { FileSearch } from "lucide-react";

// export default function EmptyState() {
//   return (
//     <div className="flex h-full min-h-[500px] items-center justify-center rounded-2xl border border-dashed border-line">
//       <div className="max-w-sm text-center">
//         <div className="relative mx-auto flex h-14 w-14 items-center justify-center rounded-full border border-line-strong">
//           <FileSearch size={24} className="text-fg-faint" />
//         </div>

//         <h2 className="mt-6 font-display text-xl font-medium text-fg">
//           No file open
//         </h2>

//         <p className="mt-3 text-sm leading-relaxed text-fg-faint">
//           Enter a company name above to assemble a research dossier — overview,
//           business model, risks, and AI opportunities, backed by sources.
//         </p>
//       </div>
//     </div>
//   );
// }




import { Building2 } from "lucide-react";

export default function EmptyState() {
    return (
        <div className="flex h-full min-h-[500px] items-center justify-center rounded-2xl border border-dashed border-[var(--border)] bg-[var(--bg-elevated)]/40">
            <div className="max-w-sm text-center">
                <span className="mx-auto flex h-14 w-14 items-center justify-center rounded-xl border border-[var(--border)] bg-[var(--surface)]">
                    <Building2 size={24} className="text-[var(--text-muted)]" />
                </span>
                <p className="font-mono mt-5 text-xs uppercase tracking-wider text-[var(--text-muted)]">
                    Awaiting input
                </p>
                <h2 className="mt-2 text-xl font-semibold text-[var(--text-primary)]">
                    No report yet
                </h2>
                <p className="mt-2 text-sm leading-6 text-[var(--text-secondary)]">
                    Enter a company name above and the agent will build a full business report — overview, challenges, and AI opportunities.
                </p>
            </div>
        </div>
    );
}




