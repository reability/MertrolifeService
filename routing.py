from Core.route import Router
from Services.Auth.controller import AuthController
from Services.User.controller import UserController
from Services.Chat.controller import WebSocket, ChatRoomController
from Services.POI.controller import POIController, POIsController


routings = [
    Router("GET", "auth", '/auth', AuthController),
    Router("GET", "ws", "/ws", WebSocket),
    Router("GET", "poi", "/poi", POIController),
    Router("*", "pois", "/pois", POIsController),
    Router("*", "user", "/user", UserController),
    Router("*", "chat-room", "/chat-room", ChatRoomController)
]
