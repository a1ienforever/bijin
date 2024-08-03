from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


from .models import CardsList, Card

name_th = ['Модель', 'Название', 'Количество', 'Цена']

#TODO: добавить фильтрацию по дате


class BijinHome(ListView):
    model = CardsList
    template_name = 'inventory_system/index.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'Главная страница',
        'name_th': name_th,
    }


def date_filter(request):
    return HttpResponse('Hello world!')

def menu(request):
    return render(request, 'inventory_system/test.html')




class CreateCard(CreateView):

    model = Card
    fields = ['num', 'name', 'price', 'note', 'photo']
    template_name = 'inventory_system/newcard.html'
    success_url = reverse_lazy('')
    extra_context = {
        'title': 'Добавление новой карточки',
    }


class AddProduct(CreateView):
    model = CardsList
    fields = ['quantity', 'model']
    template_name = 'inventory_system/addproduct.html'
    success_url = reverse_lazy('')
    extra_context = {'title': 'Добавление продукта в список'}


class Cards(ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'inventory_system/cards.html'
    extra_context = {'title': 'Список карточек'}





def shipment(request):
    return HttpResponse("Product Shipment")


