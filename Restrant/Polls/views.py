from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import Sum, F
from .models import Cart, CartItem, Item
from django.contrib import messages


def get_or_none(model, **kwargs):
    data = model.objects.filter(**kwargs)
    if data:
        return data[0]
    
    return None

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return redirect('reg')
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, 'authorization.html', {'form': form})
    
class LoginView(View):
    def get(self, request):
        return redirect('reg')
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'authorization.html', {'form': form})

def reg(request):
    return render(request, 'authorization.html')

def index(request):
    return render(request, 'index.html', context={
        'products': Item.objects.all(),
    })


class CartView(TemplateView):
    template_name = 'cart.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(
            cart__user__id=self.request.user.id
        ).annotate(
            price_sum=F('item__price') * F('quantity'),
        )
        context['cart_items'] = cart_items
        context['price_sum'] = cart_items.aggregate(sum=Sum(F('item__price') * F('quantity')))['sum'] or 0
        context['quantity_sum'] = cart_items.aggregate(sum=Sum('quantity'))['sum'] or 0
        return context

class CartItemAddView(View):
    def get(self, request: HttpRequest, product_id: int):
        if not request.user.is_authenticated:
            return redirect('login')
        
        product = get_or_none(Item, id=product_id)
        if not product:
            return redirect('index')
        
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(item=product, cart=cart, defaults={'quantity': 1})

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')

class CartItemUpdateQuantity(View):
    def get(self, request: HttpRequest, item_id: int, quantity: int):
        if not request.user.is_authenticated:
            return redirect('login')

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item = get_or_none(CartItem, cart=cart, id=item_id)

        if not cart_item:
            return redirect('cart')


        cart_item.quantity = quantity
        cart_item.save()

        return redirect('cart')


class CartItemRemoveView(View):
    def post(self, request: HttpRequest, item_id: int):
        if not request.user.is_authenticated:
            return redirect('login')

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item = get_or_none(CartItem, id=item_id, cart=cart)
        if not cart_item:
            return redirect('cart')

        cart_item.delete()

        return redirect('cart')


class CartOrderView(View):
    def get(self, request: HttpRequest, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        
        cart, _ = Cart.objects.get_or_create(user=request.user)
        CartItem.objects.filter(cart=cart).delete()
        messages.success(request, message="Вы успешно заказали добавленные товары в корзину.")
        return redirect('cart')
