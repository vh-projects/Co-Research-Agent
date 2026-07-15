const API_BASE_URL = import.meta.env.VITE_API_URL;


export async function researchCompany(companyName, onEvent) {
    const response = await fetch(`${API_BASE_URL}/research/stream`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            company_name: companyName,
        }),
    });

    if (!response.ok) {
        throw new Error("Failed to start research.");
    }

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    let buffer = "";

    while (true) {
        const { value, done } = await reader.read();

        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split("\n");

        buffer = lines.pop();

        for (const line of lines) {
            if (!line.trim()) continue;

            try {
                const event = JSON.parse(line);

                onEvent(event);
            } catch (err) {
                console.error("Failed to parse stream event:", err);
            }
        }
    }

    if (buffer.trim()) {
        try {
            onEvent(JSON.parse(buffer));
        } catch {
            // Ignore incomplete trailing data
        }
    }
}