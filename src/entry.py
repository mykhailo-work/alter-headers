from js import fetch, URL, Request, Headers

async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = env.API_HOST

    # Clone the original headers
    headers = Headers.new(request.headers)
    headers.set("Host", env.API_HOST)

    # Recreate the request with the updated URL and headers
    new_request = Request.new(
        url.toString(),
        {
            "method": request.method,
            "headers": headers,
            "body": await request.text() if request.method not in ["GET", "HEAD"] else None,
            "redirect": "manual"
        }
    )

    return await fetch(new_request)