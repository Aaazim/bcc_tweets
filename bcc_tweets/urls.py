from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tweets, name='get_tweets'),
]