from fastapi import FastAPI

from .images import images_router


docker_api = FastAPI()

docker_api.mount('/images', images_router)

__all__ = [
    'docker_api',
]
