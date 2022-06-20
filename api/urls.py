from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.users_list, name='users_list'),
]