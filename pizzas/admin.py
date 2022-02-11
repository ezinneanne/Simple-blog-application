from django.contrib import admin

# Register your models here.
from .models import Pizzas,Toppings

admin.site.register(Pizzas)
admin.site.register(Toppings)