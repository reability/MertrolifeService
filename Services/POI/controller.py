from aiohttp import web
from Services.POI.model import PointOfInterest
import json

from Logic.json_encoder import JSONEncoder

class POIController(web.View):
    async def get(self):
        data = self.request.query
        poi_id = data["id"]
        poi = await PointOfInterest(self.request.db).fetchPOIInfo(str(poi_id))
        return web.Response(content_type='application/json', text=JSONEncoder().encode(poi))


class POIsController(web.View):
    async def get(self):
        result = await PointOfInterest(self.request.db).fetchPOIAll()
        response = {"users": result}
        print(response)
        return web.Response(content_type='application/json', text=JSONEncoder().encode(response))

    async def post(self):
        data = await self.request.json()
        result = await PointOfInterest(self.request.db).create(data["poi_type"], data["title"], data["content"])
        print(result.inserted_id)
        return web.Response(content_type='application/json', text="Success")