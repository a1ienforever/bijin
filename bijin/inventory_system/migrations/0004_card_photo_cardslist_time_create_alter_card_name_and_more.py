# Generated by Django 4.2.1 on 2024-05-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_system', '0003_alter_cardslist_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photo/', verbose_name=True),
        ),
        migrations.AddField(
            model_name='cardslist',
            name='time_create',
            field=models.DateTimeField(default=None, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='card',
            name='num',
            field=models.CharField(max_length=255, unique=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
