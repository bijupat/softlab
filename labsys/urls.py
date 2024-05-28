from django.urls import path

from . import views

app_name = 'labsys'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('encounter/<int:enc_id>/', views.encounter, name='encounter'),
    path('invoice/', views.InvoiceListView.as_view(), name = 'invoice'),
    path('addpayment/', views.AddPayment, name = 'addpayment'),
    path('deletetest/', views.DeleteTest, name = 'deletetest'),
    path('addtest/<int:e_id>/<int:t_id>/', views.AddTest, name = 'addtest'),
    path('addeditdiscount/', views.AddEditDiscount, name = 'addeditdiscount'),
    path('find/', views.find, name = 'find'),
    path('search/', views.search, name = 'search'),
    path('pat_enc/<int:pat_id>/', views.pat_enc, name = 'pat_enc'),
    path('regi_Encounter/<int:pat_id>/<int:pract_id>/<int:acc_id>', views.regi_encounter, name = 'regi_encounter'),
    path('chargeitem/<int:chargeitem_id>/<str:option>', views.chargeitem, name='chargeitem'),
    path('observation_edit/', views.ObservationEdit, name = 'observationedit'),
    path('observation_verifyall/', views.ObservationVerifyAll, name = 'observationverifyall'),
    path('observation_verify/<int:ob_id>/', views.ObservationVerify, name = 'observationverify'),
    path('chargeitempreview/<pk>/', views.chargeitem_preview, name='chargeitem_preview'),
    path('observation_dataedit/<int:ob_id>/', views.ObservationDataEdit, name = 'observationdataedit'),
    path('chargeitem_dataedit/<int:ci_id>/', views.ChargeitemDataEdit, name = 'chargeitemdataedit'),
    path('regi_Appointment/<int:pat_id>/', views.regi_appointment, name = 'regi_appointment'),
    path('appointments', views.appointments, name = 'appointments'),
    path('pat_register/<int:register>/', views.pat_register, name = 'pat_register'),
    path('enc_regi_1/<int:pat_id>/', views.EnconterRegistration_1, name = 'enconterRegistration_1'),
    path('enc_regi', views.EnconterRegistration, name = 'enconterRegistration'),

]

hx_urlpatterns =[
    path('hx_search/', views.hx_search, name = 'hx_search'),
]

urlpatterns += hx_urlpatterns