# Generated by Django 3.2.16 on 2022-11-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_comment',
            field=models.TextField(default='Отсутствует', verbose_name='Комментарий для курьера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(null=True, verbose_name='Стоимость заказа'),
        ),
    ]
