from typing import List

import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs

from connect import get_responce_text


params = {"text": "python"}


async def get_pages(session, url) -> int:
	"""
	функция для получение последней страницы пагинации
	:param session:
	:param url:
	:return:
	"""
	resp = get_responce_text(session, url)
	soup = bs(resp, "lxml")
	data = soup.find_all(class_="bloko-button")
	last_page = int(data[-2].text)
	return last_page


async def get_url_vacancy(session, url: str) -> List:
	"""
	Функция для получения url каждой вакансии

	:param session:
	:param url:
	:return:
	"""
	resp = get_responce_text(session, url)
	soup = bs(resp, "lxml")
	data = soup.find_all(class_="serp-item__title")
	urls = list(map(lambda x: x.get("href"), data))
	return urls


