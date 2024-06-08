from django.urls import path
from . import  views


urlpatterns = [
    path('index/', views.IndexViews.as_view(), name='index')
]