from django.urls import path

from . import views


app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path('get_price/', views.get_price, name = 'getprice'),
]