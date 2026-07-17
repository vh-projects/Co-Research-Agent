from tavily import TavilyClient

from app.config import MAX_SEARCH_RESULTS, TAVILY_API_KEY
from app.models.search import SearchResult


class TavilyService:
    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def search(
        self,
        query: str,
        max_results: int = MAX_SEARCH_RESULTS,
    ) -> list[SearchResult]:
        response = self.client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results,
            include_answer=False,
            include_raw_content=False,
        )

        results = []

        for item in response.get("results", []):
            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    content=item.get("content", "")[:250],
                    score=item.get("score"),
                )
            )

        return results


tavily = TavilyService()


