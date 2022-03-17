from typing import List

from .__base import Model

# {
#   'Containers': -1,
#   'Created': 1647109972,
#   'Id': 'sha256:44f5e9310a12b9ff4b5ccc72eaccbfb3a6cd5bd5189bdd6a7b7d45d9d620db5c',
#   'Labels': None,
#   'ParentId': 'sha256:48872a63bf90d3584ffa4ea3d6ce08d738d39eea24405af85134ad8210cc3b99',
#   'RepoDigests': [
#       'registry.gitcommit.ru/eventlake.app/evl-collector@sha256:8dc1159b2bd8eef45e0be8898e266b91647a74bda65f7e88a0552590a3070f91'
#   ], 
#   'RepoTags': [
#       'registry.gitcommit.ru/eventlake.app/evl-collector:latest',
#       'registry.gitlab.com/eventlake.app/evl-collector:latest'
#   ],
#   'SharedSize': -1,
#   'Size': 325809838,
#   'VirtualSize': 325809838
# }


class ImageTag(Model):
    tag_name: str
    tag_id: str

    @classmethod
    def from_api(cls, data: str) -> 'ImageTag':
        return ImageTag(
            tag_id=data.split(':')[0],
            tag_name=data.split(':')[1],
        )


class Image(Model):
    image_id: str
    parent_id: str
    tags: List[ImageTag]

    @classmethod
    def from_api(cls, data: dict) -> 'Image':
        if 'RepoTags' in data and not data.get('RepoTags'):
            data['RepoTags'] = []

        return Image(
            image_id=data.get('Id'),
            parent_id=data.get('ParentId'),
            tags=[ ImageTag.from_api(t) for t in data.get('RepoTags', []) ]
        )

