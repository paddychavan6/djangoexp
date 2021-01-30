from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from .forms import registrationform,AccountAuthenticationForm,accountupdateform,logfor,CHOICES
from django.http import HttpResponse
from accounts.models import *
import face_recognition
import os
import cv2
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def index(request):
    context={}
    accounts=Account.objects.all()
    context['accounts']=accounts
    return render(request,'accounts/index.html',context)

def registeruser(request):
    context={}
    if request.POST:
        form=registrationform(request.POST,request.FILES)
        if form.is_valid():
            # form=form()
            # form.picture = form.cleaned_data["picture"]
            form.save()
            email=form.cleaned_data.get('email')
            pr=form.fields['email']
            print(pr)
            print("enything")
            raw_password=form.cleaned_data.get('password1')
            # image=form.cleaned_data.get('image')
            # url=static('R2.png')
            

            account=authenticate(email=email,password=raw_password)
            login(request,account)
            return redirect('home')
        else:
            context['registration_form']=form
    else:
        form=registrationform()
        context['registration_form']=form
    return render(request,"accounts/register.html",context)


def loginuser(request):
    context={}
    user=request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form=AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)

            if user:
                login(request,user)
                return redirect("home")

    else:
        form=AccountAuthenticationForm()

    context['login_form']=form

    return render(request,'accounts/login.html',context)

def home(request):
    return render(request,'accounts/home.html',{})

def logoutuser(request):
    logout(request)
    return redirect('index')


def account_view(request):
    url = 'accounts/templates/655.png'
    print(type(url))
    print(url)
    image=face_recognition.load_image_file(url)
    print(type(image))
    # imagecod=face_recognition.face_encodings(img)[0]
    # print("error at 2")
    location=face_recognition.face_locations(image)
    # print("error at 3")
    print(len(location))
    if not request.user.is_authenticated:
        return redirect('login')

    context={}

    if request.POST:
        form=accountupdateform(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form=accountupdateform(
            initial={
                "email":request.user.email,
                "username":request.user.username,
                "firstname":request.user.firstname,
                "lastname":request.user.lastname,
            }
        )
    context['account_form']=form
    return render(request,'accounts/account.html',context)

# def vote(request):
#     voteenable=False
#     context['status']=voteenable
#     return render(request,'accounts/vote.html',context)
# global vidname
def voter(request):
    votestatus=False
    if votestatus:
        context={}
        if request.POST:
            form=logfor(request.POST,request.FILES)
            if form.is_valid():
                global vidname
                vidname=request.POST['vid']
                form.save()
                return redirect('verifyvoter')
            else:
                context['imgform']=form
        else:
            form=logfor()
            context['imgform']=form
        return render(request,"accounts/vote.html",context)
    else:
        context={}
        context['status']='Voting is not enabled yet'
        return render(request,"accounts/vote.html",context)

def verifyvoter(request):
    context={}
    url = 'media/upload/'+vidname+'.png'
    url1='media/logupload/'+vidname+'.png'
    image=face_recognition.load_image_file(url)
    image1=face_recognition.load_image_file(url1)
    biden_encoding = face_recognition.face_encodings(image)[0]
    unknown_encoding = face_recognition.face_encodings(image1)[0]
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    if results[0]:
        context['status']=True 
        return render(request, "accounts/verifyvoter.html", context)

    else:
        context['status']=False
    return render(request,"accounts/verifyvoter.html",context)

def votedbjg(request):
    context ={}  
    urlbjp='media/votes/bjp.txt'
    with open(urlbjp, "r+") as f:
        old = f.read()
        update=int(old)+1
        f.seek(0) 
        strupdate=str(update)
        f.write(strupdate)
    return render(request, "accounts/index.html", context) 

def votedmns(request):
    context ={}  
    urlmns='media/votes/mns.txt'
    with open(urlmns, "r+") as f:
        old = f.read()
        update=int(old)+1
        f.seek(0) 
        strupdate=str(update)
        f.write(strupdate)
    return render(request, "accounts/index.html", context) 

def votedcongress(request):
    context ={}  
    urlcongress='media/votes/congress.txt'
    with open(urlcongress, "r+") as f:
        old = f.read()
        update=int(old)+1
        f.seek(0) 
        strupdate=str(update)
        f.write(strupdate)
    return render(request, "accounts/index.html", context) 
