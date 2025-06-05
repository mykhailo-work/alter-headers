from js import fetch, URL, Request, Headers

async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = env.API_HOST

    # headers = Headers.new(request.headers)
    # headers.set("Host", env.API_HOST)

    new_request = Request.new(
        request,
        {
            "redirect": "manual"
        }
    )

    return await fetch(new_request)