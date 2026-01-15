from django.urls import path

from . import views


app_name = 'website'


urlpatterns = [
   
]


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
    path('profilespreview/', views.profilespreview, name='profilespreview'),
    path('pricelistview/', views.pricelistview, name='pricelistview'),
    path('managevisit/', views.manage_visit, name='managevisit'),

    path("adddash", views.AnalyticsDashboardView, name="dashboard"), 
    path("advertisements/", views.AdvertisementListView, name="advertisement_list"),
    path("advertisements/add/", views.AdvertisementCreateView, name="advertisement_add"),
    path("links/<int:ad_id>/", views.AdLinkCreateView, name="adlink_manage"),
    path("qr/<int:link_id>/", views.QRCodeView, name="qr_code"),
    path("ad/r/<str:code>/", views.RedirectTrackingView, name="redirect_tracking"),
    # path("analytics/<int:ad_id>/", views.AnalyticsDashboardView, name="analytics"),
]