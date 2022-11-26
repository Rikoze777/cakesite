from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


FORM = [
    (1, 'Круг'),
    (2, 'Квадрат'),
    (3, 'Прямоугольник'),
]

LEVELS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
]

TOPPINGS = [
    (1, 'Без'),
    (2, 'Белый соус'),
    (3, 'Карамельный'),
    (4, 'Кленовый'),
    (5, 'Черничный'),
    (6, 'Молочный шоколад'),
    (7, 'Клубничный'),
]

BERRIES = [
    (1, 'нет'),
    (2, 'Ежевика'),
    (3, 'Малина'),
    (4, 'Голубика'),
    (5, 'Клубника'),
]

DECORS = [
    (1, 'нет'),
    (2, 'Фисташки'),
    (3, 'Безе'),
    (4, 'Фундук'),
    (5, 'Пекан'),
    (6, 'Маршмеллоу'),
    (7, 'Марципан'),
]


class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    email = models.EmailField('Email', max_length=70, blank=True, unique=True)
    phonenumber = PhoneNumberField('Номер телефона', blank=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self) -> str:
        return f"{self.name}, {self.phonenumber}"


class Cake(models.Model):
    levels = models.IntegerField('Количество уровней торта',
                                 max_length=1,
                                 choices=LEVELS,)
    form = models.IntegerField('Форма торта', max_length=2,
                               choices=FORM,)
    toppings = models.IntegerField('Топпинг', max_length=2,
                                   choices=TOPPINGS)
    berries = models.IntegerField('Ягоды', max_length=2,
                                  choices=BERRIES,
                                  default=('1', 'нет'))
    decors = models.IntegerField('Декор', max_length=2,
                                 choices=DECORS,
                                 default=('1', 'нет'))
    words = models.CharField('Надпись', max_length=50, blank=True)
    comments = models.TextField('Комментарий к заказу', blank=True)

    class Meta:
        verbose_name = 'cake'
        verbose_name_plural = 'cakes'

    def __str__(self) -> str:
        return f"{self.words}, {self.comments}"


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
    total = models.IntegerField('Стоимость заказа', null=True)
    delivery_comment = models.TextField(
        'Комментарий для курьера',
        default='Отсутствует')

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self) -> str:
        return f"{self.address}, {self.total}"


class Complaint(models.Model):
    message = models.TextField('Текст жалобы', blank=True)
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ, на который жалуются',
        related_name='complaints',
        on_delete=models.CASCADE,
        null=True)

    class Meta:
        verbose_name = 'complaint'
        verbose_name_plural = 'complaints'

    def __str__(self) -> str:
        return f"{self.order}, {self.message}"


class Promocode(models.Model):
    start_date = models.DateField('Дата начала действия промокода')
    end_date = models.DateField('Дата окончания действия промокода')
    discount = models.FloatField('Процент скидки')
    value = models.CharField('Текст промокода', max_length=50)

    class Meta:
        verbose_name = 'complaint'
        verbose_name_plural = 'complaints'

    def __str__(self) -> str:
        return f"{self.value}, {self.discount}"
