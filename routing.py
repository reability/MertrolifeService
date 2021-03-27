from Core.route import Router
from Services.Auth.controller import AuthController
from Services.User.controller import UserController

routings = [
    Router("GET", "auth", '/auth', AuthController),
    Router("*", "user", "/user", UserController)
]