class MessageFactory:
    @staticmethod
    def create_message(message_type, content):
        if message_type == 'text':
            return TextMessage(content)
        elif message_type == 'image':
            return ImageMessage(content)
        else:
            raise ValueError(f"Tipo de mensaje no soportado: {message_type}")

class TextMessage:
    def __init__(self, content):
        self.type = 'text'
        self.content = content

class ImageMessage:
    def __init__(self, content):
        self.content = content
        self.type = 'image'
