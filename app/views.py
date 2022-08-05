from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

API_KEY = '95bcdd235c90417cb39f254809479546'

# Create your views here.

def international(request):
    # Generating News
    url = f'https://newsapi.org/v2/top-headlines?language=en&apiKey={API_KEY}'
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
        print("Data not available")
        description = "Data not available"
        location = "Data not available"
        current = "Data not available"
        team1 = "Data not available"
        team2 = "Data not available"
        status = "Data not available"
        link = ""

    context = {
        'articles': articles,
        'description': description,
        'location': location,
        'status': status,
        'current': current,
        'team1': team1,
        'team2': team2,
        'link': link
    }

    return render(request, 'international.html', context)

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