import os
import aiohttp


class DockerClient:
    @classmethod
    async def request(cls, path: str, host: str = 'http://localhost', method: str = 'GET'):
        api_version = os.environ.get('API_VERSION', 'v1.40')
        socket_file = os.environ.get('UNIX_SOCKET', None)

        args = [
            method,
            f'{host}/{api_version}/{path}'
        ]
        kwargs = {}
        socket = None

        if socket_file:
            socket = aiohttp.UnixConnector(path=socket_file)
            kwargs['connector'] = socket

        try:
            async with aiohttp.request(*args, **kwargs) as resp:
                result = await resp.json()

        finally:
            if socket:
                socket.close()

        return result
