from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 50)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default=now ,blank = True)


    def __str__(self) -> str:
        return self.title + 'by' + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comments = models.TextField()
    user = models.ForeignKey(User ,on_delete = models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    parent = models.ForeignKey('self',on_delete = models.CASCADE,null = True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.comments[0:13] +"..."+ 'by                                       szW      ' + self.user.username