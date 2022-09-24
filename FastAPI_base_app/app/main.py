import time

from fastapi import FastAPI, Request

from app.routers import router
from app.auth.router import router as auth_router

app = FastAPI(
    title="Postogram",
    description=("Postogram"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
app.include_router(auth_router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):  # noqa: D103
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
