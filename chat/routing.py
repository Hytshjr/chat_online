from starlette.routing import WebSocketRoute
from .websocket_endpoints import websocket_endpoint

websocket_routes = [
    WebSocketRoute('/ws/chat/{room_name}', websocket_endpoint),
    WebSocketRoute('/ws/chat/', websocket_endpoint),
]