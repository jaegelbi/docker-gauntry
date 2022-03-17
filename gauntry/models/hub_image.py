from typing import List
from datetime import datetime

from .__base import Model


# {
#     "creator": 7,
#     "id": 2343,
#     "image_id": null,
#     "images": [
#         {
#             "architecture": "amd64",
#             "features": "",
#             "variant": null,
#             "digest": "sha256:9c152418e380c6e6dd7e19567bb6762b67e22b1d0612e4f5074bda6e6040c64a",
#             "os": "linux",
#             "os_features": "",
#             "os_version": null,
#             "size": 28565751,
#             "status": "active",
#             "last_pulled": "2022-03-17T15:37:27.361833Z",
#             "last_pushed": "2022-03-03T20:35:37.654881Z"
#         },
#         
#    ],
#    "last_updated": "2022-03-03T21:43:17.527024Z",
#    "last_updater": 1156886,
#    "last_updater_username": "doijanky",
#    "name": "latest",
#    "repository": 130,
#    "full_size": 28565751,
#    "v2": true,
#    "tag_status": "active",
#    "tag_last_pulled": "2022-03-17T16:05:36.696923Z",
#    "tag_last_pushed": "2022-03-03T21:43:17.527024Z"
# }

class HubImageTagArch(Model):
    digest: str
    arch: str

    @classmethod
    def from_api(cls, data: dict) -> 'HubImageTagArch':
        return HubImageTagArch(
            digest=data.get('digest'),
            arch=data.get('architecture'),
        )


class HubImageTag(Model):
    name: str
    images: List[HubImageTagArch]
    username: str
    updated: datetime

    @classmethod
    def from_api(cls, data: dict) -> 'HubImageTag':
        return HubImageTag(
            name=data.get('name'),
            images=[ HubImageTagArch.from_api(a) for a in data.get('images', []) ],
            username=data.get('last_updater_username'),
            updated=data.get('last_updated'),
        )
