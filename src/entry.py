from js import fetch, URL, Request

async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = env.API_HOST

    new_request = Request.new(
        url.toString(), method=request.method, headers=request.headers, body=request.body
    )

    return await fetch(new_request)