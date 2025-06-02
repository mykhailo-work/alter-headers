from js import fetch, URL

async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = env.API_HOST

    return await fetch(url.toString(), request)