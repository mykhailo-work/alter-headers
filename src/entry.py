from workers import fetch
from js import Request, Headers
from urllib.parse import urlparse, urlunparse

async def on_fetch(request):
    url = urlparse(request.url)
    modified_url = urlunparse(url._replace(netloc="pluggedtable.com"))

    new_headers = Headers.new(request.headers)
    new_headers.delete("host")

    new_request = Request.new(modified_url, {"headers": new_headers})

    return await fetch(new_request)