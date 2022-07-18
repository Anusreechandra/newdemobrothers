from django.urls import path
from . import views

app_name= 'web'

urlpatterns = [
    path("",views.index,name='index'),
   
   
    path("aboutus",views.aboutus,name='aboutus'),
    path("groupofcompany",views.groupofcompany,name='groupofcompany'),
    path("gallery",views.gallery,name='gallery'),
    path("contact",views.contact,name='contact'),
    path("product",views.product,name='product'),
]