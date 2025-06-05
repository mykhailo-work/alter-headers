from js import fetch, URL, Request, Headers

async def on_fetch(request, env):
    url = URL.new(request.url)
    
    custom_hostname = url.hostname
    url.hostname = env.API_HOST
    
    headers = Headers.new(request.headers)
    headers.set("x-manatal-custom-hostname", custom_hostname)

    new_request = Request.new(url.toString(), method=request.method, headers=headers, body=request.body)
    print(new_request.body)
    print(new_request.headers)
    print(new_request.headers.get("x-manatal-custom-hostname"))

    return await fetch(new_request)