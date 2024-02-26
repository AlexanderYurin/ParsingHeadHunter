import asyncio

from connect import get_response_text
from logger import logger
from parser.parser import get_url_vacancy, get_pages, get_data_vacancy


async def main(vacancy: str) -> None:
	tasks = []
	url_vacancy = f"https://hh.ru/search/vacancy?text={vacancy}"
	data = await get_response_text(url_vacancy)
	pages = await get_pages(data)
	logger.info(f"Получено кол-во страниц: {pages}")
	for page in range(1):
		url_page = f"https://hh.ru/search/vacancy?text={vacancy}&page={page}"
		task = asyncio.create_task(get_response_text(url_page))
		tasks.append(task)

	urls_list = await asyncio.gather(*tasks)
	urls = [url for elements in urls_list for url in elements]
	logger.info(f"Получены все страницы: {urls}")

	tasks = [asyncio.create_task(get_url_vacancy(url)) for url in urls]
	result = await asyncio.gather(*tasks)
	logger.info(f"Получены адреса: {result}")


#
# tasks = [asyncio.create_task(get_data_vacancy(url)) for url in tasks]
# await asyncio.gather(*tasks)


if __name__ == "__main__":
	try:
		asyncio.run(main("python"))
	except Exception as e:
		logger.error("Произошла ошибка: {e}")
