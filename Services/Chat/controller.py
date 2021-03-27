from aiohttp import web
from aiohttp import WSMsgType


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
                    await ws.send_str(msg.data)
                    ws_connections = self.request.app['websockets'][:]
                    ws_connections.remove(ws)
                    for ws_connection in ws_connections:
                        await ws_connection.send_str(msg.data)

            elif msg == WSMsgType.error:
                print('ws connection closed with exception %s' % ws.exception())


        self.request.app['websockets'].remove(ws)
        print('ws connection closed')
        return ws

