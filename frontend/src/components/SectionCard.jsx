// components/SectionCard.jsx

export default function SectionCard({ id, eyebrow, title, children }) {
  return (
    <section
      id={id}
      className="scroll-mt-24 rounded-2xl border border-line bg-surface p-6 sm:p-8"
    >
      <div className="mb-6 flex items-baseline gap-3 border-b border-line pb-4">
        {eyebrow && (
          <span className="font-mono text-xs tracking-widest text-marker">
            {eyebrow}
          </span>
        )}
        <h2 className="font-display text-[22px] font-medium text-fg">
          {title}
        </h2>
      </div>
      {children}
    </section>
  );
}


