// components/BulletList.jsx

export default function BulletList({ items = [] }) {
  if (!items.length) {
    return <p className="text-sm text-fg-faint">No information available.</p>;
  }

  return (
    <ul className="space-y-3.5">
      {items.map((item, index) => (
        <li key={index} className="flex gap-3">
          <span className="mt-[11px] h-px w-3 shrink-0 bg-marker/70" />
          <span className="text-[15px] leading-relaxed text-fg-muted">
            {item}
          </span>
        </li>
      ))}
    </ul>
  );
}






