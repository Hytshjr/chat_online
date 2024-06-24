from starlette.websockets import WebSocket, WebSocketDisconnect
from .connection_manager import ConnectionManager
from .messages.message_factory import MessageFactory
from .utils import parse_message

connection_manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    room_name = websocket.path_params['room_name']
    connection_manager.add_connection(room_name, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message_data = parse_message(data)
            message = MessageFactory.create_message(
                                                    message_data['messageType'],
                                                    message_data['messageContent']
                                                    )
            await connection_manager.broadcast(message, room_name)
    except WebSocketDisconnect as e:
        print(f"ADD to Log: Error: {e}")
        connection_manager.remove_connection(room_name, websocket)
