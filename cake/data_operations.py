import phonenumbers
from django.contrib.auth.models import User


def is_new_user(user_id):
     return not User.objects.filter(user_id=user_id).exists()


def save_user_data(data):
    phone = f"{data['phone_number'].country_code}{data['phone_number'].national_number}"
    User.objects.create(user_id=data["user_id"], full_name=data["full_name"], phonenumber=phone)


def validate_fullname(fullname: list) -> bool | None:
    if len(fullname) > 1:
        return True 


def validate_phonenumber(number):
    try:
        parsed_number = phonenumbers.parse(number, 'RU')
        return phonenumbers.is_valid_number_for_region(parsed_number, 'RU')
    except phonenumbers.phonenumberutil.NumberParseException:
        return False


def calculate_price(levels, form, toppings=0, berries=0, decors=0, words=''):
    level_price = (0, 400, 750, 1100)
    form_price = (0, 600, 400, 1000)
    toppings_price = (0, 0, 200, 180, 200, 300, 350, 200)
    berries_price = (0, 400, 300, 450, 500)
    decors_price = (0, 300, 400, 350, 300, 200, 280)

    total = (level_price[int(levels)] + form_price[int(form)] +
             toppings_price[int(toppings)] +
             berries_price[int(berries)] + decors_price[int(decors)])
    if words:
        total += 500
    return total


def delete_user(user_id):
    User.objects.filter(user_id__contains=user_id).delete()