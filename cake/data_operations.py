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


def delete_user(user_id):
    User.objects.filter(user_id__contains=user_id).delete()