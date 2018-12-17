from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.

# def index(request):
    # url = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=JSON'

    # headers = {'Access-Control-Allow-Origin': 'true', 'Accept': 'application/json'}

    # # r = requests.get(url, headers=headers)
    # print('testing123')
    # # print(r.text)

    # return render(request, 'vapyr_app/index.html' )

# def get_games(year, author):
#     url = 'http://api.example.com/books' 
#     params = {'year': year, 'author': author}
#     r = requests.get(url, params=params)
#     books = r.json()
#     books_list = {'books':books['results']}
#     return books_list
# req = requests.request('GET', 'https://www.giantbomb.com/api/games/?api_key=c77e7c6a04f3b3c695be65884c6ddebd6d900f70&format=json&platforms=146&sort=original_release_date:desc')


# print(req.json())