import requests
from datetime import datetime


def get_news():
    news_list = ["CPI", "Unemployment"]
    url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

    today = datetime.now().date()
    data = requests.get(url).json()
    for i in data:
        date_object = datetime.strptime(i.get('date'), "%Y-%m-%dT%H:%M:%S%z").date()
        if today == date_object and i.get("country") == "USD":
            for k in news_list:
                if k in i.get('title'):
                    return True
                
    return False



get_news()