from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encounter/<int:enc_id>/', views.encounter, name='encounter'),
    path('register', views.pat_register, name = 'PatReg' ),
    path('invoice/', views.InvoiceListView.as_view(), name = 'invoice'),
    path('addpayment/', views.AddPayment, name = 'addpayment'),
]