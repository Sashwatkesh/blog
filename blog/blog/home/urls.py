
from django.urls import path
from . views import *

urlpatterns =[
    path("",home,name="home"),
    path("about/",about,name="acout"),
    path("contact/",contact,name="contact"),
    path("search/",search,name='search'),
    path("singup",handelsingup,name='singup'),
    path('login',handlogin,name='login'),
    path('logout',handellogout,name='logout')
]