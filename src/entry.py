from workers import fetch, Response
from js import Request, Headers

# async def on_fetch(request):
#     # Create a new Headers object, copying original headers
#     new_headers = Headers.new(request.headers)
#     # Set the new Host header
#     new_headers.set("My-header", "pluggedtable.com")
    
#     # Create a new Request with the original request info and new headers
#     new_request = Request.new(request, {"headers": new_headers})
    
#     return await fetch(new_request)


async def on_fetch(request):
    new_headers = Headers.new(request.headers)
    new_headers.delete("host")

    new_headers.set("My-header", "pluggedtable.com")

    new_request = Request.new("https://pluggedtable.com", {
        "method": "GET",
        "headers": new_headers,
    })

    return await fetch(new_request)