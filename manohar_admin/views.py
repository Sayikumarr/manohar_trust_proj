from email import message
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from manohar_admin.models import FAQ, Contact, Gallery_pic, MediaPost, Poster,Event_Vol_Spon_Count,Eventschedule, Program, TeamMate, YoutubeVideo

def index_view(request):
    posts = Poster.objects.all()
    count = Event_Vol_Spon_Count.objects.all()
    events = Eventschedule.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'index.html',{'posts':posts,'count':count,'events':events,'alert':alert})
    return render(request,'index.html',{'posts':posts,'count':count,'events':events})

def about_view(request):
    faqs = FAQ.objects.all()
    teammates = TeamMate.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'about.html',{'teammates':teammates,'faqs':faqs,'alert':alert})
    return render(request,'about.html',{'teammates':teammates,'faqs':faqs})

def gallery_view(request):
    pics = Gallery_pic.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'gallery.html',{'pics':pics,'alert':alert})
    return render(request,'gallery.html',{'pics':pics})

def youtubelist_view(request):
    video = YoutubeVideo.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'youtubelist.html',{'videos':video,'alert':alert})
    return render(request,'youtubelist.html',{'videos':video})

def contact_view(request):
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'contact.html',{'alert':alert})
    return render(request,'contact.html')

def mediaCoverage_view(request):
    mediaposts = MediaPost.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'mediacoverage.html',{'mediaposts':mediaposts,'alert':alert})
    return render(request,'mediacoverage.html',{'mediaposts':mediaposts})

def ourPrograms_view(request):
    programs = Program.objects.all()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        cont = Contact(name=name,email=email,message=message)
        cont.save()
        alert.append("SENT SUCCESSFULLY!")
        return render(request,'ourPrograms.html',{'programs':programs,'alert':alert})
    return render(request,'ourPrograms.html',{'programs':programs})