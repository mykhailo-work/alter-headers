from workers import fetch, URL
from js import Request, Headers
from urllib.parse import urlparse, urlunparse

# async def on_fetch(request, env):
#     url = urlparse(request.url)
#     modified_url = urlunparse(url._replace(netloc=env.API_HOST))

#     new_headers = Headers.new(request.headers)
#     new_headers.delete("host")

#     new_request = Request.new(modified_url, {"headers": new_headers})

#     return await fetch(new_request)


async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = env.API_HOST

    return await fetch(url.toString(), request)