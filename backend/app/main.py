from fastapi import FastAPI

from app.api.routes import router


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Company Research Agent",
)


# FRONTEND_URL = os.environ.get("FRONTEND_URL")
FRONTEND_URL = os.environ.get("FRONTEND_URL")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

