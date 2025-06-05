from js import fetch, URL, Request, Headers

async def on_fetch(request, env):
    url = URL.new(request.url)
    
    custom_hostname = url.hostname
    url.hostname = env.API_HOST
    
    headers = Headers.new(request.headers)
    headers.set("x-forwarded-host", custom_hostname)

    new_request = Request.new(url.toString(), method=request.method, headers=headers, body=request.body)

    return await fetch(new_request)