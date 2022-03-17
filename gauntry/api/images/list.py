from fastapi import Request

from gauntry.repo import ImagesRepository

from .__router import images_router


@images_router.get('/')
async def list(request: Request):
    return await ImagesRepository.get_list()
