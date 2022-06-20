from django.shortcuts import render

import requests

def users_list(request):
    r = requests.get ('https://jsonplaceholder.typicode.com/users')
    data = r.json()
    return render(request, 'api/users_list.html', {'data': data})