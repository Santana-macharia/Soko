from django.urls import path

from api import restricted
from . import views
from . import restricted
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('data/', views.users_list, name='users_list'),
    path('dashboard/', views.index, name='dashboard'),
    path('restricted/', login_required (restricted.restricted_urls), name='restricted_urls'),
]