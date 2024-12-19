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


class Order(models.Model):
    id = models.AutoField(
        verbose_name="ID",
        auto_created=True,
        primary_key=True,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        to=USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        verbose_name="Пользователь"
    )

    date = models.DateTimeField(
        auto_now=True,
        null=False,
        verbose_name="Дата"
    )

    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Фамилия"
    )

    surname = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Отчество"
    )

    phone = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Телефон"
    )

    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name="E-mail"
    )

    city = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        verbose_name="Город"
    )

    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Адрес"
    )

    index = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Индекс"
    )


class OrderItem(models.Model):
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
        related_name='order_items',
    )

    quantity = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='items',
    )

    def __str__(self):
        return f"{self.item.title} - {self.quantity} шт."