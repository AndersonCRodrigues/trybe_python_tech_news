from tech_news.database import db


# Requisito 7
def search_by_title(title):
    result = db.news.find({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
