import aiohttp
import asyncio

from parser.parser import get_pages

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
						 'AppleWebKit/537.36 (KHTML, like Gecko) '
						 'Chrome/105.0.0.0 Safari/537.36 '}


async def get_responce_text(session, url: str) -> str:
	async with session.get(url, ssl=False) as resp:
		if resp.status == 200:
			return resp.text


async def get_data_page(vacancy) -> None:
	async with aiohttp.ClientSession(headers=headers) as session:
		tasks = []
		url = f"https://hh.ru/search/vacancy?text={vacancy}"
		pages = await get_pages(session, url)
		for page in range(int(pages)):
			url = f"https://hh.ru/search/vacancy?text={vacancy}&page={page}"
			task = asyncio.create_task(get_responce_text(session, url))
			tasks.append(task)
		await asyncio.gather(*tasks)


if __name__ == '__main__':
	asyncio.run(get_data_page("python"))
