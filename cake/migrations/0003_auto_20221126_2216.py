# Generated by Django 3.2.16 on 2022-11-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0002_alter_promocode_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='berries',
            field=models.IntegerField(choices=[(0, 'нет'), (1, 'Ежевика'), (2, 'Малина'), (3, 'Голубика'), (4, 'Клубника')], default=('0', 'нет'), verbose_name='Ягоды'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='decors',
            field=models.IntegerField(choices=[(0, 'нет'), (1, 'Фисташки'), (2, 'Безе'), (3, 'Фундук'), (4, 'Пекан'), (5, 'Маршмеллоу'), (6, 'Марципан')], default=('0', 'нет'), verbose_name='Декор'),
        ),
    ]
