import requests
import random
from fastapi import FastAPI

app = FastAPI()
url = 'https://api.adviceslip.com/advice'
marcus_aurelius_quotes = [
    'Если что-то кажется тебе слишком трудным, не думай, что это за пределами сил человека',
    'Начинай уже сейчас жить той жизнью, какой ты хотел бы видеть ее в конце',
    'Надо покорять умом то, что нельзя одолеть силой.'
]


@app.get('/')
def home_page():
    return 'Добро пожаловать на pet-проект Татьяны'


@app.get('/give-advice')
def give_advice():
    advice = get_advice_by_url(url)

    if advice:
        return advice
    else:
        return 'Opps'


@app.get('/give-advice/{name}')
def give_personal_advice(name):
    advice = get_advice_by_url(url)

    if advice:
        ma_quote = random.choice(marcus_aurelius_quotes)
        return '%s, мой вам совет на сегодня: %s. И совет от Марка Аврелия: %s' % (name.capitalize(), advice, ma_quote)
    else:
        return 'Opps'


def get_advice_by_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        advice = result['slip']['advice']

        return advice
    else:
        return False
