from starlette.websockets import WebSocket
import json


class ConnectionManager:
    _instance = None


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConnectionManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):
        self.connections = {}


    def add_connection(self, room_name, connection):
        if room_name not in self.connections:
            self.connections[room_name] = []
        self.connections[room_name].append(connection)


    def remove_connection(self, room_name, connection):
            if room_name in self.connections:
                self.connections[room_name].remove(connection)
                if not self.connections[room_name]:
                    del self.connections[room_name]


connection_manager = ConnectionManager()

groups = {}

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    room_name = websocket.path_params['room_name']
    connection_manager.add_connection(room_name, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            for connection in connection_manager.connections[room_name]:
                await connection.send_text(json.dumps(message))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection_manager.remove_connection(room_name, websocket)


