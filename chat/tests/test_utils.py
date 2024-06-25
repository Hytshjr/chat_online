import pytest
from chat.utils import parse_message
from chat.constants import ERROR_MESSAGE_ATRIBUTES_EMPTY, ERROR_MESSAGE_INVALID_FORMAT

def test_parse_message_valid():
    data = '{"messageType": "text", "messageContent": "Hello"}'
    result = parse_message(data)
    assert result == {'messageType': 'text', 'messageContent': 'Hello'}


def test_parse_message_missing_attributes():
    data = '{"type": "text"}'
    with pytest.raises(ValueError) as excinfo:
        parse_message(data)
    assert str(excinfo.value) == ERROR_MESSAGE_ATRIBUTES_EMPTY

def test_parse_message_invalid():
    data = 'hola'
    with pytest.raises(ValueError) as excinfo:
        parse_message(data)
    assert str(excinfo.value) == ERROR_MESSAGE_INVALID_FORMAT
