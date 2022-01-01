from django.urls import path

from . import views

app_name = 'labsys'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('encounter/<int:enc_id>/', views.encounter, name='encounter'),
    path('pat_register', views.pat_register, name = 'PatReg' ),
    path('invoice/', views.InvoiceListView.as_view(), name = 'invoice'),
    path('addpayment/', views.AddPayment, name = 'addpayment'),
    path('deletetest/', views.DeleteTest, name = 'deletetest'),
    path('addtest/', views.AddTest, name = 'addtest'),
    path('addeditdiscount/', views.AddEditDiscount, name = 'addeditdiscount'),

    

]