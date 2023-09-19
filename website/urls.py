from django.urls import path

from . import views


app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path('getprice/', views.get_price, name = 'getprice'),
    path('bookvisit/', views.book_visit, name = 'bookvisit'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('profiles/', views.profiles, name = 'profiles'),
    path('camp/', views.camp, name = 'camp'),
    path('privacy/', views.privacy, name = 'privacy'),
    path('termsconditions/', views.termsconditions, name = 'termsconditions'),

]