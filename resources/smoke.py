from sanic import response
from resources import BaseResource


class SmokeResource(BaseResource):
    async def get(self, request):
        """Simple test"""
        return response.json({"message": "ok"})
