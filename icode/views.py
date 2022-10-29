from turtle import title
from .templatetags import extras
from django.contrib import messages
from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def bloghome(request):
    obj = Post.objects.all()
    data = {
        "obj":obj
    }
    return render(request,"blog/blog.html",data)

def blogpost(request,id):
    
    obj = Post.objects.filter(slug = id).first()
    obj.views = obj.views+1
    obj.save()
    com = BlogComment.objects.filter(post = obj,parent = None)
    reply = BlogComment.objects.filter(post = obj).exclude(parent = None)
    

    repDict = {}
    for r in reply:
        if r.parent.sno not in repDict.keys():
            repDict[r.parent.sno] = [r]
        else:
            repDict[r.parent.sno].append(r)
    
    data = {
        'i':obj,
        'com':com,
        'user':request.user,
        'repDict':repDict,
    }    
    return render(request,'blog/blogslug.html',data)

def pcomment(request):
    if request.method =="POST":
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        user = request.user
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno =="":
            comment = BlogComment(comments=comment,user = user ,post = post)
            comment.save()
            messages.success(request,'Your comment has been added')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comments=comment,user = user ,post = post,parent=parent )

            comment.save()
            messages.success(request,'Your reply has been added')
        print('hii')
        return redirect(f'/icode/{post.slug}')

def createblog(request):

    if request.method=='POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        author = request.POST.get('author')
        
        

        obj = Post(title=title,desc = desc, author = author,slug = author)
        obj.save()
        return redirect('/')


    return render(request,'home/createblog.html')