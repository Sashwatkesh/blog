from tokenize import blank_re
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name= models.CharField(max_length = 100 , blank = True , null = True)
    email= models.CharField(max_length = 100,blank = True , null = True)
    phone= models.CharField(max_length = 100, blank = True , null = True)
    desc= models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True , blank = True)
    
    def __str__(self) -> str:
        return 'Message from ' + self.name 