from sanic import Sanic
from service_api import api_v1
from config import config

app = Sanic()
app.config.from_object(config['default'])
api_v1.load_api(app)
