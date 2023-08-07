import re
import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        time.sleep(1)
        return response.text if response.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    news_urls = [
        post.find("a")["href"]
        for post in soup.find_all("article", class_="entry-preview")
    ]

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", class_="next page-numbers")

    return next_page.get("href") if next_page else None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    data = {"url": soup.find("link", rel="canonical").get("href")}
    data["title"] = (
        soup.find("h1", class_="entry-title").get_text().strip(" \xa0")
    )
    data["timestamp"] = soup.find("li", class_="meta-date").get_text()
    data["writer"] = soup.find("a", class_="url fn n").get_text()
    data["summary"] = soup.find("p").get_text().strip(" \xa0")
    data["category"] = soup.find("span", class_="label").get_text()

    read_time = soup.find("li", class_="meta-reading-time").get_text()

    data["reading_time"] = int(re.findall("[0-9]+", read_time)[0])

    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
