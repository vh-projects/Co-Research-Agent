from pprint import pprint

from app.graph.builder import graph


result = graph.invoke(
    {
        "company_name": "NVIDIA"
    }
)

print(result.keys())
# pprint(result["report"].model_dump())