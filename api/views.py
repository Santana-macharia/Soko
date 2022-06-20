from django.shortcuts import render

# Create your views here.

def users_list(request):
    return render(request, 'api/users_list.html', {})