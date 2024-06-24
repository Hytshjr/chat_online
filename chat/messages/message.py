from chat.constants import ERROR_MESSAGE_EMPTY


class Message:
    def __init__(self, message_type, content):
        self.type = message_type
        self.content = content
        self.error = ERROR_MESSAGE_EMPTY

    def to_dict(self):
        message = {"messageType": self.type, "messageContent": self.content}
        if not self.content:
            message["errorMessage"] = self.error
        return message