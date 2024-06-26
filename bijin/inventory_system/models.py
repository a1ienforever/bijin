import time

from django.db import models


class CardsList(models.Model):
    quantity = models.IntegerField()
    model = models.ForeignKey('Card', on_delete=models.CASCADE, related_name='cards')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


class Card(models.Model):
    num = models.CharField(max_length=255, unique=True, verbose_name="Модель:")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    name = models.CharField(max_length=255, verbose_name="Название:")
    price = models.IntegerField(verbose_name="Цена:")
    photo = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name="Фото:")
    note = models.CharField(max_length=510, verbose_name='Заметка:', blank=True, default='')

    def __str__(self):
        return self.num
