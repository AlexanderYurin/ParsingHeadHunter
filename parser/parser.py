import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs

from connect import get_responce_text

params = {"text": "python"}


async def get_pages(session, vacancy: str) -> str:
	"""
	функция для получение последней страницы пагинации
	:param session:
	:param vacancy:
	:return:
	"""
	resp = get_responce_text(session, "https://hh.ru/search/vacancy?text={vacancy}")
	soup = bs(resp, "lxml")
	pages = soup.find_all()
	last_page = pages[-1].text
	return last_page


