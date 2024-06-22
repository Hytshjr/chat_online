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


    async def broadcast(self, content: str, room_name):
        for connection in self.connections[room_name]:
            await connection.send_text(json.dumps(content))
