from datetime import datetime
import phonenumbers

from django.shortcuts import render
from django.utils import dateparse
from .models import Cake, User, Order
from .data_operations import validate_phonenumber, calculate_price
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    if request.GET:
        received_data = request.GET
        levels = received_data.get("LEVELS")
        form = received_data.get("FORM")
        toppings = received_data.get("TOPPING")
        berries = received_data.get("BERRIES")
        decors = received_data.get("DECOR")
        berries = berries if berries else 0
        decors = decors if decors else 0
        words = received_data.get("WORDS")
        words = words if words else 'отсутствует'
        comments = received_data.get("COMMENTS")
        created_cake, new_cake = Cake.objects.get_or_create(
            levels=levels,
            form=form,
            toppings=toppings,
            berries=berries,
            decors=decors,
            words=words,
            comments=comments)
        cake = created_cake if created_cake else new_cake
        name = received_data.get("NAME")
        email = received_data.get("EMAIL")
        phonenumber = received_data.get("PHONE")
        if validate_phonenumber(phonenumber):
            phonenumber = phonenumbers.parse(phonenumber, 'RU')
            phonenumber = phonenumbers.format_number(
                phonenumber,
                phonenumbers.PhoneNumberFormat.E164
            )
        created_user, new_user = User.objects.get_or_create(
            name=name,
            phonenumber=phonenumber,
            email=email)
        user = created_user if created_user else new_user
        order_datetime = datetime.now()
        delivery_date = dateparse.parse_date(received_data.get("DATE"))
        delivery_time = dateparse.parse_time(received_data.get("TIME"))
        delivery_datetime = datetime.combine(delivery_date, delivery_time)
        address = received_data.get("ADDRESS")
        total = calculate_price(levels, form, toppings, berries, decors, words)
        delivery_comment = received_data.get('DELIVCOMMENTS')
        delivery_comment = delivery_comment if delivery_comment else 'Отсутствует'
        Order.objects.create(
            user=user,
            order_datetime=order_datetime,
            delivery_datetime=delivery_datetime,
            address=address,
            cake=cake,
            total=total,
            delivery_comment=delivery_comment)
    return render(request, "index.html")


@require_http_methods(['POST'])
def login_page(request):
    try:
        payload = request.POST
        phonenumber = payload.get('phonenumber')
        if validate_phonenumber(phonenumber):
            phonenumber = phonenumbers.parse(phonenumber, 'RU')
            phonenumber = phonenumbers.format_number(
                phonenumber,
                phonenumbers.PhoneNumberFormat.E164
            )
        user = User.objects.get(phonenumber=phonenumber)
    except ObjectDoesNotExist:
        return render(request, 'without_lk.html')

    orders = user.orders.all()
    context = {
        'client_details': {
            'phone': str(phonenumber),
            'name': user.name,
            'email': user.email,
        },
        'orders': orders,
    }
    return render(request, 'lk-order.html', context)
