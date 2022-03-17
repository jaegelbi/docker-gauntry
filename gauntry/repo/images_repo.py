from typing import List

from gauntry.models import Image, HubImageTag
from gauntry.helpers import DockerClient, DockerHubClient


class ImagesRepository:
    @classmethod
    async def get_list(cls) -> List[Image]:
        images = await DockerClient.request('images/json')

        return [ Image.from_api(image) for image in images ]

    @classmethod
    async def get_tags_from_hub(cls, library: str, image_name: str, page_size: int = 10, page_no: int = 1) -> List[HubImageTag]:
        tags = await DockerHubClient.get_tags(library, image_name, page_size, page_no)

        return [ HubImageTag.from_api(tag) for tag in tags ]
