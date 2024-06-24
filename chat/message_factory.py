import json


class Message:
    def __init__(self, message_type, content):
        self.type = message_type
        self.content = content

    def to_dict(self):
        return {"type": self.type, "content": self.content}


class MessageFactory:
    @staticmethod
    def create_message(message_type, content):
            if message_type == 'text':
                message = TextMessage(content)
            elif message_type == 'image':
                message = ImageMessage(content)
            else:
                raise ValueError(f"Tipo de mensaje no soportado: {message_type}")

            return json.dumps(message.to_dict())


class TextMessage(Message):
    def __init__(self, content):
        super().__init__('text', content)

class ImageMessage(Message):
    def __init__(self, content):
        super().__init__('image', content)
