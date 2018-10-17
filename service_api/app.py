from sanic import Sanic

from service_api import api_v1

app = Sanic()
api_v1.load_api(app)
