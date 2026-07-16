

import json

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.encoders import jsonable_encoder

from app.graph.builder import graph
from app.models.request import ResearchRequest
from app.models.response import ResearchResponse
from app.utils.progress import NODE_STATUS

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
)
def research(request: ResearchRequest):
    try:
        result = graph.invoke(
            {
                "company_name": request.company_name,
            }
        )

        return ResearchResponse(
            success=True,
            report=result["report"],
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# @router.post("/research/stream")
# def research_stream(request: ResearchRequest):

#     def generate():

#         final_report = None

#         yield json.dumps(
#             {
#                 "type": "start",
#                 "message": "Starting research...",
#             }
#         ) + "\n"

#         for event in graph.stream(
#             {
#                 "company_name": request.company_name,
#             },
#             stream_mode="updates",
#         ):

#             for node_name, state in event.items():

#                 yield json.dumps(
#                     {
#                         "type": "progress",
#                         "node": node_name,
#                         "message": NODE_STATUS.get(node_name, node_name),
#                     }
#                 ) + "\n"

#                 if "report" in state:
#                     final_report = state["report"]

#         yield json.dumps(
#             {
#                 "type": "complete",
#                 "report": final_report.model_dump(),
#             }
#         ) + "\n"

#     return StreamingResponse(
#         generate(),
#         media_type="application/x-ndjson",
#     )

@router.post("/research/stream")
def research_stream(request: ResearchRequest):

    def generate():

        final_report = None

        yield json.dumps({
            "type": "start"
        }) + "\n"

        for event in graph.stream(
            {"company_name": request.company_name},
            stream_mode="updates",
        ):

            # event = {"validator": {...}}
            node_name = next(iter(event.keys()))
            state = event[node_name]

            yield json.dumps({
                "type": "completed",
                "node": node_name,
            }) + "\n"

            if "report" in state:
                final_report = state["report"]

        if final_report is not None:

            yield json.dumps(
                jsonable_encoder({
                    "type": "complete",
                    "report": final_report,
                })
            ) + "\n"

    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson",
    )


