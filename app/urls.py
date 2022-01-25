from django.views.generic.base import View
from gamezone.settings import MEDIA_ROOT, MEDIA_URL
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # main page 

    # path('',views.home),
    path('',views.productview.as_view(),name='home'),
    path('contact/',views.contact,name='contact'),

    # in gaming devices page
    path('gaming_computer/',views.gaming_computer,name='gaming_computer'),
    path('gaming_laptops/',views.gaming_laptops,name='gaming_laptops'),
    path('gaming_mobiles/',views.gaming_mobiles,name='gaming_mobiles'),
    path('search/',views.search,name='search'),

    path('gaming_headphone/',views.gaming_headphone,name='gaming_headphone'),
    path('gaming_moniter/',views.gaming_moniter,name='gaming_moniter'),
    path('keybord_mouse/',views.keybord_mouse,name='keybord_mouse'),
    path('products/<str:slug>',views.products,name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
