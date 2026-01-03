from django.urls import path

from . import views

app_name = 'labsys'
urlpatterns = [
    # url_view_mastersheet updated urls
    path('', views.index, name='index'),
    path('add_request_1/<int:pat_id>/', views.add_request_1, name= 'add-request-1'),
    path('add_request_2/<int:pat_id>/<int:plist_id>/<int:pract_id>/', views.add_request_2, name= 'add-request-2'),
    path('service_requests/', views.servicerequests, name= 'service-requests'),
    path('add_enc/<int:req_id>', views.add_encounter, name = 'add-encounter'),

    # url_view_mastersheet not updated urls
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
    path('chargeitem/<int:chargeitem_id>/<str:option>', views.chargeitem, name='chargeitem'),
    path('observation_edit/', views.ObservationEdit, name = 'observationedit'),
    path('observation_verifyall/', views.ObservationVerifyAll, name = 'observationverifyall'),
    path('observation_verify/<int:ob_id>/', views.ObservationVerify, name = 'observationverify'),
    path('chargeitempreview/<pk>/', views.chargeitem_preview, name='chargeitem_preview'),
    path('observation_dataedit/<int:ob_id>/', views.ObservationDataEdit, name = 'observationdataedit'),
    path('chargeitem_dataedit/<int:ci_id>/', views.ChargeitemDataEdit, name = 'chargeitemdataedit'),
    path('regi_Appointment/<int:pat_id>/', views.regi_appointment, name = 'regi_appointment'),
    path('appointments', views.appointments, name = 'appointments'),
]

hx_urlpatterns =[

    # url_view_mastersheet updated urls
    path(f'hx_patsrch/', views.hx_patient_search, name = 'patient-search'),

    # url_view_mastersheet updated urls

]

urlpatterns += hx_urlpatterns


'''
guideline for naming route and name of url
everything in small case 
view  with _ seperator
name wiht - seperator
urlpatterns = [
    path("index/", views.index, name="main-view"),
    path("bio/<username>/", views.bio, name="bio"),
    path("articles/<slug:title>/", views.article, name="article-detail"),
    path("articles/<slug:title>/<int:section>/", views.article_section, name="article-section"),
    path("blog/", include("blog.urls")),
    ...,
]
'''