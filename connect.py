import aiohttp
import asyncio

from config import HEADERS


async def get_response_text(url: str) -> str:
	async with aiohttp.ClientSession(headers=HEADERS) as session:
		async with session.get(url, ssl=False) as resp:
			if resp.status == 200:
				resp_text = await resp.text()
				return resp_text


