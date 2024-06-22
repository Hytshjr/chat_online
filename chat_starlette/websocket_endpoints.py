from starlette.websockets import WebSocket
import json

# In-memory storage for groups (for simplicity, not suitable for production)
groups = {}

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    room_name = websocket.query_params.get('room_name')
    room_group_name = f'chat_{room_name}'

    if room_group_name not in groups:
        groups[room_group_name] = []

    groups[room_group_name].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)  # Parse the received message
            # Send message to all in the group
            for connection in groups[room_group_name]:
                await connection.send_text(json.dumps(message))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        groups[room_group_name].remove(websocket)
        if not groups[room_group_name]:
            del groups[room_group_name]
