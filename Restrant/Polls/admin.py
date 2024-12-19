from django.contrib import admin
from .models import Cart, CartItem, Item, Order

# Register your models here.


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Item)
admin.site.register(Order)