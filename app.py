from unittest import loader
from aiohttp import web
from routes import setup_routes, setup_static_routes
import aiohttp_jinja2
import jinja2

app = web.Application()
aiohttp_jinja2.setup(app, loader = jinja2.FileSystemLoader('templates'))
setup_routes(app)
setup_static_routes(app)
web.run_app(app)

if __name__ == '__main__':
    print('test')

