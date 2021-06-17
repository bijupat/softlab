from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encounter/<int:enc_id>/', views.encounter, name='encounter'),
    path('register', views.pat_register, name = 'PatReg' )
]