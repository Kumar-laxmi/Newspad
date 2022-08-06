from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup

API_KEY = '95bcdd235c90417cb39f254809479546'

# Create your views here.

def general(request):
    # Generating News
    url = f'https://newsapi.org/v2/top-headlines?category=general&language=en&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    # Generating Live Cricket Score
    html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text
    soup = BeautifulSoup(html_text, "html.parser")
    sect = soup.find_all('div', class_='sp-scr_wrp')
    section = sect[0]
    description = section.find('span', class_='description').text
    location = section.find('span', class_='location').text
    current = section.find('div', class_='scr_dt-red').text
    link = "https://sports.ndtv.com/" + \
        section.find('a', class_='scr_ful-sbr-txt').get('href')
    try:
        dataFoundCricket = True
        status = section.find_all('div', class_="scr_dt-red")[1].text
        block = section.find_all('div', class_='scr_tm-wrp')
        team1_block = block[0]
        team1_name = team1_block.find('div', class_='scr_tm-nm').text
        team1_score = team1_block.find('span', class_='scr_tm-run').text
        team2_block = block[1]
        team2_name = team2_block.find('div', class_='scr_tm-nm').text
        team2_score = team2_block.find('span', class_='scr_tm-run').text
        team1 = team1_name.strip() + ":" + team1_score.strip()
        team2 = team2_name.strip() + ":" + team2_score.strip()
    except:
        print("Cricket data not available")
        dataFoundCricket = False
        description = "Data not available"
        location = "Data not available"
        current = "Data not available"
        team1 = "Data not available"
        team2 = "Data not available"
        status = "Data not available"
        link = ""
    
    # Generating live cryto currency price
    # Defining Binance API URL
    key = "https://api.binance.com/api/v3/ticker/price?symbol="

    # Making list for multiple crypto's
    currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT", "ETHUSDT", "BNBUSDT", "USDCUSDT"]
    # We need: BitCoin, Ethereum, Tether, USD Coin, Binance Coin

    # Blank JSON 
    crypto_data = []

    # running loop to print all crypto prices
    try:
        dataFoundCrypto = True
        for i in currencies:
            # completing API for request
            url = key+i 
            data_temp = requests.get(url)
            data_temp = data_temp.json()
            crypto_data.append(data_temp)
    except:
        print("Crypto Data not found")
        dataFoundCrypto = False

    context = {
        'articles': articles,
        'dataFoundCricket': dataFoundCricket,
        'description': description,
        'location': location,
        'status': status,
        'current': current,
        'team1': team1,
        'team2': team2,
        'link': link,
        'dataFoundCrypto': dataFoundCrypto,
        'crypto_data': crypto_data
    }

    return render(request, 'general.html', context)

def national(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'national.html', context)

def sports(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'sports.html', context)

def business(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'business.html', context)

def entertainment(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    
    context = {
        'articles': articles
    }

    return render(request, 'entertainment.html', context)

def health(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'health.html', context)

def science(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'science.html', context)

def technology(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'technology.html', context)