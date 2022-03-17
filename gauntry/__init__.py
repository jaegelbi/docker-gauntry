import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gauntry.api import docker_api


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount('/docker', docker_api)
