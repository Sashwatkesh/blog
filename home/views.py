from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from icode.models import Post
from django.http import HttpResponse
from . models import *
from django.shortcuts import render,redirect
from django.contrib import messages
from icode.models import Post
# Create your views here.
def home(request):
    obj = Post.objects.filter().order_by('-views')[:3]
    data = {
        'obj':obj
    }
    print(obj)
    return render(request,"home/index.html",data)


def about(request):
    return render(request,"home/about.html")


def contact(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')


        if len(name)<2 or len(email)<3 or len(phone)<4:
            messages.error(request,'invalid data')

        else:
            messages.error(request,'Message has been send ')

            contact_obj = Contact(name = name,email = email, phone = phone , desc = desc)
            contact_obj.save()

        return redirect('/contact')


    return render(request,"home/contact.html")


def search(request):
    subj = request.GET.get('query')
    if len(subj) > 80:
        obj = Post.objects.none()
    else:

        obcontent = Post.objects.filter(desc__icontains=subj)
        objtitle = Post.objects.filter(title__icontains=subj)
        obj = obcontent.union(objtitle)
    if obj.count() == 0:
        messages.error (request,"No Sesrch result found")
    data = {
        'subj':subj,
        "obj":obj
        }

    return render (request,"home/search.html",data)

def handelsingup(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
# Check for input
        if not username.isalnum():
            return render(request,"Name should onlu contain letters and numbers ")

        if password!=password2:
            messages.error(request,"Password don't match")
            return redirect("")
        if len(username) > 10:
            messages.error(request,"To long username")

#create user
    
        myuser = User.objects.create_user(username, email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save
        messages.success(request,"Your Account Has Been Created")
        return redirect("/")

    else:
        return HttpResponse("404 not-allowed")

def handlogin(request):
    
    if request.method=='POST':
        logusername = request.POST.get('username')
        logpassword = request.POST.get('password')

        user = authenticate(username = logusername,password = logpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Login")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect("/")

    return HttpResponse("login")

def handellogout(request):
    logout(request)
    messages.success(request,"Sucessfully Logout")

    return redirect("/")
