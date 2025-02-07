import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "K1core.settings")
django.setup()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from django.core.asgi import get_asgi_application
from blocks.api import router as blocks_router

app = FastAPI(title="Crypto Blocks API")

django_asgi_app = get_asgi_application()


@app.get("/")
def root():
    return {"message": "Test task"}

app.mount("/static", StaticFiles(directory="staticfiles"), name="static")
app.mount("/django", django_asgi_app)

app.include_router(blocks_router, prefix="/api")
