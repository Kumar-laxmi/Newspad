from django.shortcuts import render
import requests

from newsapi import NewsApiClient

API_KEY = '95bcdd235c90417cb39f254809479546'

# Create your views here.

def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'index.html', context)