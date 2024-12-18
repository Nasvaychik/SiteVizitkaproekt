from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.

USER_MODEL = get_user_model()

class Cart(models.Model):
    id = models.AutoField(
        verbose_name="ID",
        auto_created=True,
        primary_key=True,
        null=False,
    )

    user = models.OneToOneField(
        to=USER_MODEL,
        null=False,
        unique=True,
        blank=False,
        on_delete=models.CASCADE,
    )

class Item(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        null=False,
    )

    price = models.IntegerField(
        default=0,
        help_text="Цена в коп.",
        null=False,
        blank=False,
    )

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,   
    )

    photo = models.ImageField(
        null=True,
        blank=True,
    )

    

class CartItem(models.Model):
    id = models.AutoField(
        verbose_name="ID",
        auto_created=True,
        primary_key=True,
        blank=True,
        null=False,
    )

    item = models.ForeignKey(
        to=Item,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='cart_items', 
    )

    quantity = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )

    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='items',
    )