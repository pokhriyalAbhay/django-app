from django.contrib import admin
from django.urls import path , include
from newapp import views

urlpatterns =[

    path("",views.index, name='newapp'),
    path("contact",views.contact, name='contact'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services')
   
]
    