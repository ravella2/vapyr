from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

# Create your views here.

def index(request):
    url = 'https://www.giantbomb.com/api/games/?api_key=6e0060f42d81f489256e472989988c2b69e0eacc&format=JSON'

    headers = {'Access-Control-Allow-Origin': 'true', 'Accept': 'application/json'}

    # r = requests.get(url, headers=headers)
    print('testing123')
    # print(r.text)

    return render(request, 'vapyr_app/index.html' )
