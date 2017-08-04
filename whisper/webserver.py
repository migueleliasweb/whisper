import credstash
from aiohttp import web, web_request

async def get_secret(request: web_request.Request):
    secret_key = request.match_info.get("key")
    secret_value = credstash.getSecret(secret_key)
    return web.Response(text="Secret key retrieved: "+secret_value)

async def set_secret(request: web_request.Request):
    secret_key = request.match_info.get("key")
    data = await request.json()
    next_version = credstash.paddedInt(credstash.getHighestVersion(name=secret_key))
    credstash.putSecret(name=secret_key,secret=data["value"], version=next_version)
    return web.Response(text="Secret key stored: "+secret_key)

def setup_routes(app: web.Application):
    app.router.add_get('/secret/{key}', get_secret)
    app.router.add_post('/secret/{key}', set_secret)

def run():
    app = web.Application()
    setup_routes(app)

    web.run_app(app, host='127.0.0.1', port=8080)
