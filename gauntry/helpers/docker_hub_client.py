import aiohttp


class DockerHubClient:
    @classmethod
    async def get_tags(cls, library: str, image_name: str, page_size: int = 10, page_no: int = 1):
        url = f'https://hub.docker.com/v2/repositories/{library}/{image_name}/tags/?page_size={page_size}&page={page_no}'

        async with aiohttp.request('GET', url) as resp:
            result = await resp.json()

        return result.get('results', [])
