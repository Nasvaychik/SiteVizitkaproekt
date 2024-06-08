from django.urls import path
from . import views
from .views import RegisterView, LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.reg, name='reg'),
    path('register/reg/', RegisterView.as_view(), name='register'),
    path('register/login/', LoginView.as_view(), name='login')
]