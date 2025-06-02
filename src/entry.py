from workers import Response, fetch

async def on_fetch(request):
    return await fetch(request)

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