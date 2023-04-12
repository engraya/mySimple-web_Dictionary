from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name='homePage'),#this is the search url
    path('DictionaryPage', views.DictionaryPage, name='DictionaryPage'),#this is the search url
]
