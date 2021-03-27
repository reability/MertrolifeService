from aiohttp import web
from Services.User.model import User

from Logic.json_encoder import JSONEncoder

class UserController(web.View):
    async def get(self):
        data = self.request.query
        user_id = data["id"]
        user = await User(self.request.db).fetchUserInfo(str(user_id))
        return web.Response(content_type='application/json', text=JSONEncoder().encode(user))

    async def post(self):
        data = await self.request.json()
        await User(self.request.db).create(data["name"], data["login"], data["password"])

        return web.Response(content_type='application/json', text="Success")