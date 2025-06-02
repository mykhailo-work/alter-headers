from workers import fetch
from js import Request, Headers

async def on_fetch(request):
    # Create a new Headers object, copying original headers
    new_headers = Headers.new(request.headers)
    # Set the new Host header
    new_headers.set("Host", "pluggedtable.com")
    
    # Create a new Request with the original request info and new headers
    new_request = Request.new(request, {"headers": new_headers})
    
    return await fetch(new_request)


# async def on_fetch(request):
#     response = await fetch("https://example.com")

#     # Grab the response headers so they can be modified
#     new_headers = response.headers

#     # Add a custom header with a value
#     new_headers["x-workers-hello"] = "Hello from Cloudflare Workers"

#     # Delete headers
#     if "x-header-to-delete" in new_headers:
#         del new_headers["x-header-to-delete"]
#     if "x-header2-to-delete" in new_headers:
#         del new_headers["x-header2-to-delete"]

#     # Adjust the value for an existing header
#     new_headers["x-header-to-change"] = "NewValue"

#     return Response(response.body, headers=new_headers)