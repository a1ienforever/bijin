from datetime import datetime
from typing import List, Any

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from .forms import AddCardForm, AddProduct
from .models import Card, CardsList

name_th = ['Модель', 'Название', 'Количество', 'Цена']

#TODO: добавить фильтрацию по дате
def index(request):
    cards = CardsList.objects.all()
    dict = request.POST
    print(dict)
    data = {'title': 'Главная страница',
            'trs': cards,
            'name_th': name_th,
            }

    return render(request, 'inventory_system/index.html', context=data)

# def int_to_date(date: dict, request):
#     from_to = list()
#     date1 = date['from_date'].split('-')
#     date1 = map(int, date1)
#     date1 = list(date1)
#     date1 = datetime(date1[0], date1[1], date1[2])
#     from_to.append(date1)
#     date2 = date['to_date'].split('-')
#     date2 = map(int, date2)
#     date2 = list(date2)
#     date2 = datetime(date2[0], date2[1], date2[2])
#     from_to.append(date2)
#     return from_to

def date_filter(request):

    return HttpResponse('Hello world!')


def create_card(request):
    if request.method == 'POST':
        form = AddCardForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save() #Добавление в базу данных
            return redirect('')
    else:
        form = AddCardForm()

    data = {
        'title': 'Добавление новой карточки',
        'form': form
    }
    return render(request, 'inventory_system/newcard.html', context=data)


# def accept_create(request):
#     card_num = request.POST['cardNumber']
#     name = request.POST['name']
#     price = request.POST['price']
#     card = Card(num=card_num, name=name, price=price)
#     card.save()
#     return render(request, 'inventory_system/accept.html')


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save() # Добавление в базу данных
            return redirect('')
    else:
        form = AddProduct()

    data = {
        'title': 'Добавление товара',
        'form': form
    }
    return render(request, 'inventory_system/addproduct.html', context=data)


def shipment(request):
    return HttpResponse("Product Shipment")


def cards(request):
    return render(request, 'inventory_system/cards.html')