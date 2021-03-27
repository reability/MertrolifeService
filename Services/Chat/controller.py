from aiohttp import web
from aiohttp import WSMsgType

import json

from .model import ChatRoom
from Logic.json_encoder import JSONEncoder


class WebSocket(web.View):
    async def get(self):

        ws = web.WebSocketResponse()
        await ws.prepare(self.request)
        await ws.send_str('hello my dear mister Popponi')

        self.request.app['websockets'].append(ws)

        async for msg in ws:
            if msg.type == WSMsgType.text:
                if msg.data == 'close':
                    await ws.close()
                else:
                    await ws.send_str(json.loads(msg.data)["text"])

                    if ChatRoom(self.request.db).fetchChatRoom(json.loads(msg.data)["user_id"]):
                        pass

                    ws_connections = self.request.app['websockets'][:]
                    ws_connections.remove(ws)
                    for ws_connection in ws_connections:
                        await ws_connection.send_str(msg.data)

            elif msg == WSMsgType.error:
                print('ws connection closed with exception %s' % ws.exception())


        self.request.app['websockets'].remove(ws)
        print('ws connection closed')
        return ws

class ChatRoomController(web.View):
    async def get(self):
        data = self.request.query
        user_id = data["user_id"]
        chat_room = await ChatRoom(self.request.db).fetchChatRoom(str(user_id))
        return web.Response(content_type='application/json', text=JSONEncoder().encode(chat_room))

    async def post(self):
        data = await self.request.json()
        result = await ChatRoom(self.request.db).create(data["user_id"])
        print(result.inserted_id)
        return web.Response(content_type='application/json', text="Success")

    async def update(self):
        data = await self.request.json()
        result = await ChatRoom(self.request.db).update(data["user_id"], data["message"])
        print(result)
        return web.Response(content_type='application/json', text="Success")
