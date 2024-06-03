# Generated by Django 4.2.1 on 2024-05-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_system', '0005_alter_cardslist_time_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='note',
            field=models.CharField(default=None, max_length=510, null=True, verbose_name='Заметка:'),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название:'),
        ),
        migrations.AlterField(
            model_name='card',
            name='num',
            field=models.CharField(max_length=255, unique=True, verbose_name='Модель:'),
        ),
        migrations.AlterField(
            model_name='card',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/', verbose_name='Фото:'),
        ),
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(verbose_name='Цена:'),
        ),
    ]
