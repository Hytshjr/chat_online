from starlette.websockets import WebSocket, WebSocketDisconnect
from .connection_manager import ConnectionManager
from .message_factory import MessageFactory
import json

connection_manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    room_name = websocket.path_params['room_name']
    connection_manager.add_connection(room_name, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            message_type = message_data.get('type')
            content = message_data.get('content')
            message_factory = MessageFactory.create_message(message_type, content)
            message_factory = json.loads(json.dumps(message_factory.__dict__))
            await connection_manager.broadcast(message_factory, room_name)
    except WebSocketDisconnect as e:
        print(f"ADD to Log: Error: {e}")
        connection_manager.remove_connection(room_name, websocket)
