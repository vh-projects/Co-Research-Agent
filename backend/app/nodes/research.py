from concurrent.futures import ThreadPoolExecutor, as_completed
from app.services.tavily_search import tavily
from app.state import ResearchState


SEARCH_QUERIES = [
    "{} company overview",
    "{} products and services",
    "{} business model",
    "{} technology stack",
    "{} latest news",
    "{} AI initiatives",
]


def research_node(state: ResearchState) -> ResearchState:
    company_name = state["company_name"]

    all_results = []
    seen_urls = set()

    def search(query: str):
        return tavily.search(query.format(company_name))

    with ThreadPoolExecutor(max_workers=len(SEARCH_QUERIES)) as executor:
        futures = [
            executor.submit(search, query)
            for query in SEARCH_QUERIES
        ]

        for future in as_completed(futures):
            results = future.result()

            for result in results:
                url = str(result.url)

                if url in seen_urls:
                    continue

                seen_urls.add(url)
                all_results.append(result)
    
    all_results.sort(
    key=lambda x: x.score or 0,
    reverse=True,)

    all_results = all_results[:10]

    return {
        "progress": "Research completed.",
        "search_results": all_results,
    }

