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
    path('addtest/<int:e_id>/<int:t_id>/', views.AddTest, name = 'addtest'),
    path('addeditdiscount/', views.AddEditDiscount, name = 'addeditdiscount'),
    path('find/', views.find, name = 'find'),
    path('search/', views.search, name = 'search'),
    path('pat_enc/<int:pat_id>/', views.pat_enc, name = 'pat_enc'),
    path('regi_old_pat/<int:pat_id>/', views.regi_old_pat, name = 'regi_old_pat'),
    path('chargeitem/<int:chargeitem_id>/<str:option>', views.chargeitem, name='chargeitem'),
    path('observation_edit/', views.ObservationEdit, name = 'observationedit'),
    path('observation_verifyall/', views.ObservationVerifyAll, name = 'observationverifyall'),
    path('observation_verify/<int:ob_id>/', views.ObservationVerify, name = 'observationverify'),
    path('chargeitempreview/<pk>/', views.chargeitem_preview, name='chargeitem_preview'),
    path('observation_dataedit/<int:ob_id>/', views.ObservationDataEdit, name = 'observationdataedit'),
    path('chargeitem_dataedit/<int:ci_id>/', views.ChargeitemDataEdit, name = 'chargeitemdataedit'),

    

]