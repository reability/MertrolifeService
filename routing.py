from Core.route import Router
from Services.Auth.controller import AuthController
from Services.User.controller import UserController
from Services.Chat.controller import WebSocket

routings = [
    Router("GET", "auth", '/auth', AuthController),
    Router("*", "user", "/user", UserController),
    Router("GET", "chat", "/ws", WebSocket)
]