from typing import List
from bs4 import BeautifulSoup as bs


async def get_pages(data: str) -> int:
	"""
	Функция для получения последней страницы пагинации
	:param data: полученные данные с сайта
	:return: возвращает кол-во страниц
	"""
	soup = bs(data, "lxml")
	data = soup.find_all("a", class_="bloko-button", )
	last_page = int(data[-2].text)
	return last_page


async def get_url_vacancy(data: str) -> List:
	"""
	Функция для получения url каждой вакансии
	:param data: полученные данные с сайта
	:return: возвращает список адресов вакансий
	"""
	soup = bs(data, "lxml")
	data = soup.find("main", class_="vacancy-serp-content")
	data = data.find_all("a", class_="bloko-link")
	urls = list(map(lambda x: x.get("href"), data))
	return urls


async def get_data_vacancy(data: str) -> List:
	"""
	Функция для получения ключевых навыков вакансии
	:param data: полученные данные с сайта
	:return: возвращает ключевые навыки
	"""
	soup = bs(data, "lxml")
	data = soup.find_all("span", class_="bloko-tag__section")
	skills = list(map(lambda x: x.text, data))
	return skills
# async with aiofiles.open("data.txt", "a+", encoding="utf-8") as f:
# 	if skills:
# 		await f.write(" ".join(skills) + "\n")
