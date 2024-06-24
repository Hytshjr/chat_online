import json


def parse_message(data):
    try:
        message_data = json.loads(data)
        if 'type' not in message_data or 'content' not in message_data:
            raise ValueError("El mensaje debe contener 'type' y 'content'")
        return message_data
    except json.JSONDecodeError as e:
        raise ValueError("Mensaje con formato incorrecto") from e
