# import random
import requests
from fastapi import FastAPI

app = FastAPI()

colleagues = ['Saken', 'Aliya', 'Shinbolat']

colleagues_db = {
    'Saken': {
        'room_number': '504',
        'age': 28,
    },
    'Aliya': {
        'room_number': '504',
        'age': 28,
    },
    'Shinbolat': {
        'room_number': '327',
        'age': 28,
    }
}
countries = ['Japan', 'Egypt', 'Iran', 'Turkish', 'France']

countries_db = {
    'Japan': {
        'population': '125 410 000',
        'city': 'Tokyo',
        'president': 'Haryhito'
    },
    'Egypt': {
        'population': '102 079 960	',
        'city': 'Kair',
        'president': 'Abdul-fattah As-sisi'
    },
    'Iran': {
        'population': '85 194 842',
        'city': 'Tegeran',
        'president': 'Hasan Ryhani'
    },
    'Turkish': {
        'population': '83 154 997',
        'city': 'Ankara',
        'president': 'Redjep Tayip Erdogan'
    },
    'France': {
        'population': '68 859 599',
        'city': 'Paris',
        'president': 'Emmanyel Makron'
    }
}


class RequestAPI:
    url = 'https://api.quotable.io/random'

    def get_quote(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            quote = response.json()
            return quote
        else:
            return 'Qate'

    def get_content(self):
        quote = self.get_quote()
        return quote['content']

    def get_text_with_quote_for_name(self, name):
        result = 'Hi %s. You must read this text: %s' % (name.capitalize(), self.get_content())
        return result


@app.get('/countries')
def countries():
    return countries_db


@app.get('/countries/{name}')
def countries(name):
    if name in countries_db:
        return countries_db[name]
    else:
        return 'Qate'


# quote
@app.get('/quotes/{name}')
def colleagues(name):
    my_request = RequestAPI()
    return my_request.get_text_with_quote_for_name(name)
