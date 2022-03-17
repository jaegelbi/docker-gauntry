from fastapi import Request

from gauntry.repo import ImagesRepository

from .__router import images_router


@images_router.get('/{library}/{image}/tags/{page_size}/{page_no}')
async def tags(request: Request):
    library = request.path_params.get('library')
    image = request.path_params.get('image')
    page_size = request.path_params.get('page_size')
    page_no = request.path_params.get('page_no')

    return await ImagesRepository.get_tags_from_hub(library, image, page_size, page_no)
