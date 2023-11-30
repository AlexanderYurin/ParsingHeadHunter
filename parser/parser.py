from typing import List

import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs

from connect import get_response_text


async def get_pages(session, url) -> int:
	"""
	Функция для получения последней страницы пагинации
	:param session:
	:param url:
	:return:
	"""
	resp = await get_response_text(session, url)
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
	resp = await get_response_text(session, url)
	soup = bs(resp, "lxml")
	data = soup.find_all(class_="serp-item__title")
	urls = list(map(lambda x: x.get("href"), data))
	return urls


async def get_data_vacancy(session, url: str) -> List:
	"""
	Функция для получения ключевых навыков вакансии

	:param session:
	:param url:
	:return:
	"""
	resp = await get_response_text(session, url)
	soup = bs(resp, "lxml")
	data = soup.find_all(class_="bloko-tag__section bloko-tag__section_text")
	skills = list(map(lambda x: x.text, data))
	return skills
