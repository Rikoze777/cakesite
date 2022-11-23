from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    email = models.EmailField('Email', max_length=70, blank=True, unique=True)
    phonenumber = PhoneNumberField('Номер телефона', blank=True)


class Cake(models.Model):
    levels = models.IntegerField('Количество уровней торта', default=1)
    form = models.CharField('Форма торта', max_length=50)
    topping = models.CharField(
        'Топпинг',
        max_length=50,
        default='Без топпинга')
    berries = models.CharField('Ягоды', max_length=50, default='Без ягод')
    decor = models.CharField('Декор', max_length=50, default='Без декора')
    words = models.CharField('Надпись', max_length=50, blank=True)
    comments = models.TextField('Комментарий к заказу', blank=True)


class Order(models.Model):
    order_datetime = models.DateTimeField('Дата и время заказа')
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='orders',
        on_delete=models.CASCADE)
    address = models.TextField(
        'Адрес доставки',
        help_text='г.Ярославль, ул. Звёздная, д.5 кв.4')
    cake = models.ForeignKey(
        Cake,
        verbose_name='Заказанный торт',
        related_name='orders',
        on_delete=models.CASCADE)
    delivery_datetime = models.DateTimeField('Дата и время доставки')
    total = models.IntegerField('Стоимость заказа')


class Complaint(models.Model):
    message = models.TextField('Текст жалобы', blank=True)
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ, на который жалуются',
        related_name='complaints',
        on_delete=models.CASCADE,
        null=True)


class Promocode(models.Model):
    start_date = models.DateField('Дата начала действия промокода')
    end_date = models.DateField('Дата окончания действия промокода')
    discount = models.FloatField('Процент скидки')
    value = models.CharField('Текст промокода', max_length=50)
