import json


class MessageFactory:
    @staticmethod
    def create_message(message_type, content):
            if message_type == 'text':
                message = TextMessage(content)
            elif message_type == 'image':
                message = ImageMessage(content)
            else:
                raise ValueError(f"Tipo de mensaje no soportado: {message_type}")

            return json.loads(json.dumps(message.__dict__))


class TextMessage:
    def __init__(self, content):
        self.type = 'text'
        self.content = content


class ImageMessage:
    def __init__(self, content):
        self.content = content
        self.type = 'image'
