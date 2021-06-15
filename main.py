import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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


class RequestCOVID:
    url = 'https://api.covid19api.com/summary'
    payload = {}
    headers = {}

    def get_covid(self):
        payload = {}
        headers = {}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        if response.status_code == 200:
            all_info = response.json()
            return all_info
        else:
            return 'Qate'


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


@app.get('/', response_class=HTMLResponse)
async def read_items(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/about', response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get('/quotes')
async def just_qoute(request: Request):
    my_request_quote = RequestAPI()
    text = my_request_quote.get_content()
    link_text = "generation by site('https://api.quotable.io/random')..."
    return templates.TemplateResponse("quotes.html", {
        "request": request, "name": text, "link_text": link_text})


@app.get('/quotes/{name}', response_class=HTMLResponse)
async def read_item(request: Request, name):
    name_col = name
    my_request = RequestAPI()
    text = my_request.get_content()
    return templates.TemplateResponse("quotes.html", {
        "request": request, "name": name_col + ', this is quot for you', "text": text})


@app.get('/pandemic', response_class=HTMLResponse)
async def read_pandemic(request: Request):
    my_request = RequestCOVID()
    global_stat_info = my_request.get_covid()
    Global = global_stat_info['Global']
    NewConfirmed = Global['NewConfirmed']
    TotalConfirmed = Global['TotalConfirmed']
    t_mln = str(TotalConfirmed)[0:3]
    t_min = str(TotalConfirmed)[3:6]
    t_n = str(TotalConfirmed)[6:9]
    NewDeaths = Global['NewDeaths']
    TotalDeaths = Global['TotalDeaths']
    d_mln = str(TotalDeaths)[0:1]
    d_min = str(TotalDeaths)[1:4]
    d_n = str(TotalDeaths)[4:7]
    NewRecovered = Global['NewRecovered']
    TotalRecovered = Global['TotalRecovered']
    rec_mln = str(TotalRecovered)[0:3]
    rec_min = str(TotalRecovered)[3:6]
    rec_n = str(TotalRecovered)[6:9]
    Date = Global['Date'].split("T")
    Dates = Date[1].split(".")

    return templates.TemplateResponse("pandemic.html",
                                      {"request": request,
                                       "NewConfirmed": NewConfirmed,
                                       "TotalConfirmed": t_mln+" million "+t_min+" thousand "+t_n,
                                       "NewDeaths": NewDeaths,
                                       "TotalDeaths": d_mln+" million "+d_min+" thousand "+d_n,
                                       "NewRecovered": NewRecovered,
                                       "TotalRecovered": rec_mln+" million "+rec_min+" thousand "+rec_n,
                                       "Day": Date[0],
                                       "Time": Dates[0]
                                       })


@app.get('/countries/{name}')
def countries(request: Request, name):
    if name in countries_db:
        name_countries = name
        info = countries_db[name]
        pop = info['population']
        city = info['city']
        pres = info['president']
        return templates.TemplateResponse("country.html", {
            "request": request,
            "name": name_countries,
            "pop": pop,
            "city": city,
            "pres": pres
        })
    else:
        return 'Qate'
