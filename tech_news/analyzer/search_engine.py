from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    result = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError("Data inválida") from e

    formatted_date = date.strftime("%d/%m/%Y")

    result = db.news.find({"timestamp": formatted_date})

    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
