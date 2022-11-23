from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=50)
    email = models.EmailField('Email', max_length=70, blank=True, unique=True)
    phonenumber = PhoneNumberField('Номер телефона', blank=True)

    def __str__(self) -> str:
        return f"@{self.name}, {self.phonenumber}"


class Cake(models.Model):
    class Form(models.TextChoices):
        ROUND = "ROUND"
        SQUARE = "SQUARE"
        RECTANGLE = "RECTANGLE"
        NO = "NO"

    class Levels(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3

    class Toppings(models.TextChoices):
        WITHOUT = "WITHOUT"
        WHITE = "WHITE"
        CARAMEL = "CARAMEL"
        MAPLE = "MAPLE"
        BLUEBERRY = "BLUEBERRY"
        MILKCHOCKOLATE = "MILKCHOCKOLATE"
        STAWBERRY = "STAWBERRY"
        NO = "NO"

    class Berries (models.TextChoices):
        STAWBERRY = "STAWBERRY"
        BLUEBERRY = "BLUEBERRY"
        RAPSBERRY = "RAPSBERRY"
        BLACKBERRY = "BLACKBERRY"
        NO = "NO"

    class Decors (models.TextChoices):
        PISTACHIO = "PISTACHIO"
        MERINGUE = "MERINGUE"
        HAZELNUT = "HAZELNUT"
        PECAN = "PECAN"
        MARSHMALLOW = "MARSHMALLOW"
        MARZIPAN = "MARZIPAN"
        NO = "NO"

    levels = models.IntegerField('Количество уровней торта',
                                 choices=Levels.choices,
                                 default=Levels.ZERO)
    form = models.CharField('Форма торта', max_length=50,
                            choices=Form.choices,
                            default=Form.NO)
    toppings = models.CharField('Топпинг', max_length=50,
                                choices=Toppings.choices,
                                default=Toppings.NO)
    berries = models.CharField('Ягоды', max_length=50,
                               choices=Berries.choices,
                               default=Berries.NO)
    decors = models.CharField('Декор', max_length=50,
                              choices=Decors.choices,
                              default=Decors.NO)
    words = models.CharField('Надпись', max_length=50, blank=True)
    comments = models.TextField('Комментарий к заказу', blank=True)

    def __str__(self) -> str:
        return f"@{self.words}, {self.comments}"


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

    def __str__(self) -> str:
        return f"@{self.address}, {self.total}"


class Complaint(models.Model):
    message = models.TextField('Текст жалобы', blank=True)
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ, на который жалуются',
        related_name='complaints',
        on_delete=models.CASCADE,
        null=True)

    def __str__(self) -> str:
        return f"@{self.order}, {self.message}"


class Promocode(models.Model):
    start_date = models.DateField('Дата начала действия промокода')
    end_date = models.DateField('Дата окончания действия промокода')
    discount = models.FloatField('Процент скидки')
    value = models.CharField('Текст промокода', max_length=50)

    def __str__(self) -> str:
        return f"@{self.value}, {self.discount}"
