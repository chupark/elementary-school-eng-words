from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from . import config

from .routers import words
settings = config.Settings()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="800 English words for elementary students",
        version="1.0.0",
        openapi_version="3.0.0",
        description="초등학생을 위한 필수 어휘 800제",
        servers=[
            {
                "url": settings.API_URL
            }
        ],
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app = FastAPI()
app.include_router(words.router)
app.openapi = custom_openapi