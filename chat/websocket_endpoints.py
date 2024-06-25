from starlette.websockets import WebSocket, WebSocketDisconnect
from .connection_manager import ConnectionManager
from .messages.message_factory import MessageFactory
from .error_handler import error_handler
from .utils import parse_message
from .logger import logger

connection_manager = ConnectionManager()

@error_handler
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    room_name = websocket.path_params['room_name']
    connection_manager.add_connection(room_name, websocket)
    logger.info(f"Connected to room {room_name}")

    try:
        while True:
            data = await websocket.receive_text()
            message_data = parse_message(data)
            message = MessageFactory.create_message(
                                                    message_data['messageType'],
                                                    message_data['messageContent']
                                                    )
            await connection_manager.broadcast(message, room_name)
            logger.debug(f"Message sent in room {room_name} from user")

    except WebSocketDisconnect as e:
        logger.info(f"User disconnected from room {room_name}")
        connection_manager.remove_connection(room_name, websocket)

    except Exception as e:
        logger.error(f"Unexpected error in room {room_name}: {e}")
        raise e
