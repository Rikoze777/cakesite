from django.contrib import admin
from .models import (
    User,
    Cake,
    Order,
    Complaint,
    Promocode,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "phonenumber")


@admin.register(Cake)
class UserAdmin(admin.ModelAdmin):
    list_display = ("words", "comments")


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ("address", "total")
    raw_id_fields = ("cake", "user")

@admin.register(Complaint)
class UserComplaint(admin.ModelAdmin):
    list_display = ("order", "message")


@admin.register(Promocode)
class Promocode(admin.ModelAdmin):
    list_display = ("value", "discount")