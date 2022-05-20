from django.conf.urls import url, include
from SP1 import views
from django.urls import path

urlpatterns=[
    url(r'^nutzer$',views.NutzerApi),
    #url(r'^nutzer/(?P<str>[-\w]+)$', views.NutzerApi),
    #path('testnutzer/', views.NutzerApiTest),
    url(r'^nutzer/([0-9]+)$',views.NutzerApi),
    path('nutzer/<str:username>',views.NutzerApi),
    path('userlogin/', views.userlogin),
]