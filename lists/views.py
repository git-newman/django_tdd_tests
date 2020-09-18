from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    """домашняя страница"""
    if request.POST.get('item_text', False) is not False:
        context = {'item_text': request.POST.get('item_text')}
    else:
        context = {}

    print(context)

    return render(request, 'home.html', context)
