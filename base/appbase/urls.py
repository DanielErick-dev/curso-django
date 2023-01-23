from django.urls import path
from . import views

app_name = 'appbase'
urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home')]