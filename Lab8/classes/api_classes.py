import requests
from datetime import datetime
from colorama import Fore

class NewsAPI:
    BASE_URL = "https://newsapi.org/v2/"
    
    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_headlines(self, country='us'):
        url = f"{self.BASE_URL}top-headlines?country={country}&apiKey={self.api_key}"
        return self._make_request(url)

    def search_news(self, keyword):
        url = f"{self.BASE_URL}everything?q={keyword}&apiKey={self.api_key}&pageSize=10"
        return self._make_request(url)

    def _make_request(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.status_code}")
        return response.json()

class Repository:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def get_all(self):
        return self.data

class UnitOfWork:
    def __init__(self):
        self.repository = Repository()

    def commit(self):
        pass

class History:
    def __init__(self):
        self.queries = []

    def add_query(self, query, result_count):
        self.queries.append({
            "timestamp": datetime.now(),
            "query": query,
            "result_count": result_count
        })

    def display(self):
        for query in self.queries:
            print(f"{query['timestamp']} - Query: '{query['query']}', Results: {query['result_count']}")

class UserInterface:
    def __init__(self, api):
        self.api = api
        self.uow = UnitOfWork()
        self.history = History()
        self.title_color = Fore.WHITE  # Default color