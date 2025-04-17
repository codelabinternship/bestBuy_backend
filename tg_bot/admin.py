from django.contrib import admin
from django.contrib import admin
from .models import User, Orders, OrderItem, Products, Categories

admin.site.register(User)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(Products)
admin.site.register(Categories)

# Register your models here.
