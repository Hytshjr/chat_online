import pytest
import websockets
import json


@pytest.mark.asyncio
async def test_websocket_communication():
    uri = "ws://127.0.0.1:8000/ws/chat/2"
    async with websockets.connect(uri) as websocket:
        # Enviar un mensaje
        await websocket.send(json.dumps({"messageType": "text", "messageContent": "Hello, world!"}))

        # Recibir el mensaje
        response = await websocket.recv()
        response_data = json.loads(response)
        assert response_data == {"messageType": "text", "messageContent": "Hello, world!"}

@pytest.mark.asyncio
async def test_websocket_disconnect():
    uri = "ws://127.0.0.1:8000/ws/chat/2"
    async with websockets.connect(uri) as websocket:
        await websocket.close()

        # Verificar que la conexión se ha cerrado correctamente
        assert websocket.closed
        assert websocket.close_code == 1000
