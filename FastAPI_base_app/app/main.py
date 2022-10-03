import time

from fastapi import FastAPI, Request

from app.routers import router as main_router
from app.auth.auth_router import auth_router
from .containers import Container


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI(
        title="Postogram",
        description=("Postogram"),
        version="0.0.1",
        docs_url="/docs",
        redoc_url="/docs/redoc",
    )
    app.container = container
    app.include_router(main_router)
    app.include_router(auth_router)
    return app


app = create_app()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):  # noqa: D103
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
