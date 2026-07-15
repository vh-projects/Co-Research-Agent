export default function GeneratingState() {
    return (
        <div className="space-y-4">
            {[0, 1, 2].map((i) => (
                <div
                    key={i}
                    className="rounded-2xl border border-[var(--border)] bg-[var(--bg-elevated)] p-6"
                    style={{ animationDelay: `${i * 80}ms` }}
                >
                    <div className="animate-shimmer mb-4 h-4 w-40 rounded" />
                    <div className="animate-shimmer mb-2 h-3 w-full rounded" />
                    <div className="animate-shimmer h-3 w-4/5 rounded" />
                </div>
            ))}
        </div>
    );
}