// components/ReportViewer.jsx

import { Building2, Briefcase, Cpu, Newspaper, AlertTriangle, Lightbulb, Target } from "lucide-react";
import SectionCard from "./SectionCard";
import BulletList from "./BulletList";
import EmptyState from "./EmptyState";
import SourceList from "./SourceList";

const NAV = [
  { id: "overview", label: "Overview" },
  { id: "business", label: "Business" },
  { id: "stack", label: "Stack" },
  { id: "news", label: "News" },
  { id: "challenges", label: "Challenges" },
  { id: "opportunities", label: "Opportunities" },
  { id: "pitch", label: "Pitch" },
  { id: "sources", label: "Sources" },
];

export default function ReportViewer({ report }) {
  if (!report) return <EmptyState />;

  const { evidence, overview, business, challenges, ai_opportunities, ceo_pitch } = report;

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap gap-2 rounded-2xl border border-line bg-surface p-3">
        {NAV.map((item) => (
          <a
            key={item.id}
            href={`#${item.id}`}
            className="rounded-lg px-3 py-1.5 font-mono text-xs text-fg-faint transition-colors hover:bg-surface-2 hover:text-marker"
          >
            {item.label}
          </a>
        ))}
      </div>

      <SectionCard id="overview" eyebrow="01" title="Company overview">
        <div className="flex items-start gap-3">
          <Building2 size={18} className="mt-1 shrink-0 text-marker" />
          <p className="leading-7 text-fg-muted">{overview.summary}</p>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-5 border-t border-line pt-6">
          {[
            ["Industry", evidence.industry],
            ["Headquarters", evidence.headquarters],
            ["Founded", evidence.founded],
            ["Company size", evidence.company_size],
          ].map(([label, value]) => (
            <div key={label}>
              <h3 className="mb-1.5 font-mono text-xs uppercase tracking-wider text-fg-faint">
                {label}
              </h3>
              <p className="text-sm text-fg">{value}</p>
            </div>
          ))}
        </div>
      </SectionCard>

      <SectionCard id="business" eyebrow="02" title="Business overview">
        <div className="mb-3 flex items-center gap-2">
          <Briefcase size={15} className="text-marker" />
          <h3 className="font-semibold text-fg">Core operations</h3>
        </div>
        <BulletList items={business.core_operations} />

        <h3 className="mb-3 mt-7 font-semibold text-fg">Revenue streams</h3>
        <BulletList items={business.revenue_streams} />

        <h3 className="mb-3 mt-7 font-semibold text-fg">Customer segments</h3>
        <BulletList items={business.customer_segments} />
      </SectionCard>

      <SectionCard id="stack" eyebrow="03" title="Technology stack">
        <div className="mb-3 flex items-center gap-2">
          <Cpu size={15} className="text-marker" />
          <h3 className="font-semibold text-fg">Observed technologies</h3>
        </div>
        <BulletList items={evidence.technologies_used} />
      </SectionCard>

      <SectionCard id="news" eyebrow="04" title="Recent news">
        <div className="space-y-5">
          {evidence.recent_news.map((news, index) => (
            <div key={index} className="border-l-2 border-marker/50 pl-4">
              <div className="flex items-center gap-2">
                <Newspaper size={14} className="text-fg-faint" />
                <h3 className="font-semibold text-fg">{news.title}</h3>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-fg-muted">{news.summary}</p>
              <p className="mt-2 font-mono text-xs text-fg-faint">{news.source}</p>
            </div>
          ))}
        </div>
      </SectionCard>

      <SectionCard id="challenges" eyebrow="05" title="Business challenges">
        <div className="space-y-4">
          {challenges.challenges.map((challenge, index) => (
            <div key={index} className="rounded-xl border border-line bg-surface-2 p-4">
              <div className="flex items-center gap-2">
                <AlertTriangle size={15} className="text-danger" />
                <h3 className="font-semibold text-fg">{challenge.title}</h3>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-fg-muted">{challenge.description}</p>
              <span className="mt-4 inline-block rounded-md bg-danger/15 px-2.5 py-1 font-mono text-xs text-danger">
                Impact — {challenge.impact}
              </span>
            </div>
          ))}
        </div>
      </SectionCard>

      <SectionCard id="opportunities" eyebrow="06" title="AI opportunities">
        <div className="space-y-4">
          {ai_opportunities.opportunities.map((item, index) => (
            <div key={index} className="rounded-xl border border-line bg-surface-2 p-4">
              <div className="flex items-center gap-2">
                <Lightbulb size={15} className="text-marker" />
                <h3 className="font-semibold text-fg">{item.title}</h3>
              </div>
              <p className="mt-2 text-sm leading-relaxed text-fg-muted">{item.description}</p>

              <div className="mt-4 flex flex-wrap gap-2">
                <span className="rounded-md bg-marker/15 px-2.5 py-1 font-mono text-xs text-marker">
                  {item.priority}
                </span>
                <span className="rounded-md bg-signal/15 px-2.5 py-1 font-mono text-xs text-signal">
                  {item.implementation_complexity}
                </span>
              </div>

              <p className="mt-4 text-sm leading-relaxed text-fg-muted">{item.business_value}</p>
            </div>
          ))}
        </div>
      </SectionCard>

      <SectionCard id="pitch" eyebrow="07" title="Executive recommendation">
        <div className="flex items-start gap-3">
          <Target size={18} className="mt-1 shrink-0 text-marker" />
          <p className="leading-7 text-fg-muted">{ceo_pitch.executive_summary}</p>
        </div>

        <div className="mt-6 border-t border-line pt-6">
          <h3 className="mb-3 font-semibold text-fg">Recommended initiatives</h3>
          <BulletList items={ceo_pitch.recommended_ai_initiatives} />
        </div>

        <div className="mt-7">
          <h3 className="mb-3 font-semibold text-fg">Expected business impact</h3>
          <BulletList items={ceo_pitch.expected_business_impact} />
        </div>

        <div className="mt-7 rounded-xl border border-signal/30 bg-signal/10 p-5">
          <h3 className="font-mono text-xs uppercase tracking-wider text-signal">
            Recommended first step
          </h3>
          <p className="mt-3 text-sm leading-relaxed text-fg">{ceo_pitch.recommended_first_step}</p>
        </div>
      </SectionCard>

      <SectionCard id="sources" eyebrow="08" title="Sources">
        <SourceList citations={evidence.citations} />
      </SectionCard>
    </div>
  );
}

