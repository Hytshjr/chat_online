import pytest
from chat.connection_manager import ConnectionManager

class MockWebSocket:
    def __init__(self):
        self.messages = []

    async def send_text(self, content):
        self.messages.append(content)

@pytest.fixture
def connection_manager():
    ConnectionManager._instance = None
    return ConnectionManager()

def test_add_connection(connection_manager):
    websocket = MockWebSocket()
    room_name = "room1"

    connection_manager.add_connection(room_name, websocket)
    assert room_name in connection_manager.connections
    assert websocket in connection_manager.connections[room_name]

def test_remove_connection(connection_manager):
    websocket = MockWebSocket()
    room_name = "room1"

    connection_manager.add_connection(room_name, websocket)
    assert room_name in connection_manager.connections
    connection_manager.remove_connection(room_name, websocket)
    assert room_name not in connection_manager.connections


@pytest.mark.asyncio
async def test_broadcast(connection_manager):
    websocket1 = MockWebSocket()
    websocket2 = MockWebSocket()
    room_name = "room1"
    message = "Hello, world!"

    connection_manager.add_connection(room_name, websocket1)
    connection_manager.add_connection(room_name, websocket2)
    await connection_manager.broadcast(message, room_name)

    assert message in websocket1.messages
    assert message in websocket2.messages
