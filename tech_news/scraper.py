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
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
