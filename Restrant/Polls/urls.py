from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import RegisterView, LoginView, CartView, CartItemAddView, CartItemRemoveView, CartItemUpdateQuantity, \
    CartOrderView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.reg, name='reg'),
    path('register/reg/', RegisterView.as_view(), name='register'),
    path('register/login/', LoginView.as_view(), name='login'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/item/add/<int:product_id>', CartItemAddView.as_view(), name='add_to_cart'),
    path('cart/item/remove/<int:item_id>/', CartItemRemoveView.as_view(), name='remove_from_cart'),
    path('cart/item/update-quantity/<int:item_id>/<int:quantity>/', CartItemUpdateQuantity.as_view(), name='update_quantity'),
    path('cart/order/', CartOrderView.as_view(), name='order_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)