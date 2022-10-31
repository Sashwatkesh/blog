from django.urls import path
from .views import*


urlpatterns = [

    path("createblog/",createblog,name="createblog"),
   
    path("pcomment/",pcomment,name="pcomment"),
    
    path("",bloghome, name="bloghome"),
    
    path("/<id>",blogpost,name="blogpost"),
]