# test_parser.py

import pytest
import asyncio
# import aiohttp
# from unittest.mock import AsyncMock, patch
from parser.parser import get_pages, get_url_vacancy, get_data_vacancy


@pytest.mark.asyncio
async def test_get_pages():
    data = """
    <div class="pagination">
        <a class="bloko-button" href="#">1</a>
        <a class="bloko-button" href="#">2</a>
        <a class="bloko-button" href="#">3</a>
    </div>
    """
    assert await get_pages(data) == 2


@pytest.mark.asyncio
async def test_get_url_vacancy():
    data = """
    <main class="vacancy-serp-content">
        <a class="bloko-link" href="/vacancy/1">Job 1</a>
        <a class="bloko-link" href="/vacancy/2">Job 2</a>
    </main>
    """
    assert await get_url_vacancy(data) == ["/vacancy/1", "/vacancy/2"]


@pytest.mark.asyncio
async def test_get_data_vacancy():
    data = """
    <span class="bloko-tag__section">Python</span>
    <span class="bloko-tag__section">Django</span>
    """
    assert await get_data_vacancy(data) == ["Python", "Django"]


# @pytest.mark.asyncio
# async def test_write_to_file():
#     # Mocking the open function
#     with patch("builtins.open", create=True) as mock_open:
#         # Mocking the file object
#         mock_file = AsyncMock()
#         mock_open.return_value.__aenter__.return_value = mock_file
#
#         # Simulating the skills data
#         skills = ["Python", "Django"]
#         await write_to_file(skills)
#
#         # Asserting that the write method was called with the correct data
#         mock_file.write.assert_awaited_once_with("Python Django\n")
#
#
# # Add more tests or modify them based on your requirements

