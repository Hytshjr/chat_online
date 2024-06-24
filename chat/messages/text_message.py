from .message import Message


class TextMessage(Message):
    def __init__(self, content):
        super().__init__('text', content)