import pytest
from unittest.mock import patch
from chat.error_handler import error_handler
from chat.logger import logger

@error_handler
async def function_that_raises():
    raise ValueError("This is a test error")

@error_handler
async def function_that_succeeds():
    return "Success"

@pytest.mark.asyncio
async def test_error_handler_with_exception():
    with patch.object(logger, 'error') as mock_logger:
        with pytest.raises(ValueError) as excinfo:
            await function_that_raises()
        assert str(excinfo.value) == "This is a test error"
        mock_logger.assert_called_once_with("Error in function_that_raises: This is a test error", exc_info=True)

@pytest.mark.asyncio
async def test_error_handler_without_exception():
    result = await function_that_succeeds()
    assert result == "Success"
