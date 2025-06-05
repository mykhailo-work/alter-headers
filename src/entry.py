from js import fetch, URL, Request, Response


async def on_fetch(request, env):
    url = URL.new(request.url)
    
    custom_hostname = url.hostname
    url.hostname = env.API_HOST

    new_request = Request.new(
        url.toString(),
        {
            "method": request.method,
            "headers": request.headers,
            "body": await request.text() if request.method not in ["GET", "HEAD"] else None,
            "redirect": "manual"
        }
    )
    
    response = await fetch(new_request)
    
    new_headers = response.headers
    new_headers["x-custom-hostname"] = custom_hostname

    return Response(response.body, headers=new_headers)