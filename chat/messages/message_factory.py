from chat.constants import ERROR_MESSAGE_UNSUPPORTED_TYPE
from .image_message import ImageMessage
from .text_message import TextMessage
import json

class MessageFactory:
    @staticmethod
    def create_message(message_type, content):
        if message_type == 'text':
            message = TextMessage(content)
        elif message_type == 'image':
            message = ImageMessage(content)
        else:
            raise ValueError(f"{ERROR_MESSAGE_UNSUPPORTED_TYPE}: {message_type}")
        return json.dumps(message.to_dict())