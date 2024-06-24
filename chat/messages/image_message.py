from .message import Message


class ImageMessage(Message):
    def __init__(self, content):
        super().__init__('image', content)