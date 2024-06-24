from .constants import ERROR_MESSAGE_INVALID_FORMAT, ERROR_MESSAGE_ATRIBUTES_EMPTY
import json


def parse_message(data):
    try:
        message_data = json.loads(data)
        if 'messageType' not in message_data or 'messageContent' not in message_data:
            raise ValueError(ERROR_MESSAGE_ATRIBUTES_EMPTY)
        return message_data
    except json.JSONDecodeError as e:
        raise ValueError(ERROR_MESSAGE_INVALID_FORMAT) from e
