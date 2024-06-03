# Generated by Django 4.2.1 on 2024-04-24 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_system.card')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductCard',
        ),
    ]
