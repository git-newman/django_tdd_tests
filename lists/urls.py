from .views import *
from django.urls import path

app_name = 'lists'

urlpatterns = [
    path('', home_page, name='home'),
]
