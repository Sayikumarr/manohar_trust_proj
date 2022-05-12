from django.shortcuts import render
from manohar_admin.forms import captchaForm
from manohar_admin.models import FAQ, Contact, Gallery_pic, MediaPost, Poster,Event_Vol_Spon_Count,Eventschedule, Program, TeamMate, YoutubeVideo

def index_view(request):
    posts = Poster.objects.all()
    count = Event_Vol_Spon_Count.objects.all()
    events = Eventschedule.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'index.html',{'posts':posts,'count':count,'events':events,'alert':alert,'captcha':captcha})
    return render(request,'index.html',{'posts':posts,'count':count,'events':events,'captcha':captcha})

def about_view(request):
    faqs = FAQ.objects.all()
    teammates = TeamMate.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'about.html',{'teammates':teammates,'faqs':faqs,'alert':alert,'captcha':captcha})
    return render(request,'about.html',{'teammates':teammates,'faqs':faqs,'captcha':captcha})

def gallery_view(request):
    pics = Gallery_pic.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'gallery.html',{'pics':pics,'alert':alert,'captcha':captcha})
    return render(request,'gallery.html',{'pics':pics,'captcha':captcha})

def youtubelist_view(request):
    video = YoutubeVideo.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'youtubelist.html',{'videos':video,'alert':alert,"captcha":captcha})
    return render(request,'youtubelist.html',{'videos':video,'captcha':captcha})

def contact_view(request):
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'contact.html',{'alert':alert,'captcha':captcha})
    return render(request,'contact.html',{'captcha':captcha})

def mediaCoverage_view(request):
    mediaposts = MediaPost.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'mediacoverage.html',{'mediaposts':mediaposts,'alert':alert,'captcha':captcha})
    return render(request,'mediacoverage.html',{'mediaposts':mediaposts,'captcha':captcha})

def ourPrograms_view(request):
    programs = Program.objects.all()
    captcha=captchaForm()
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        captcha=captchaForm(request.POST)
        if captcha.is_valid():
            cont = Contact(name=name,email=email,message=message)
            cont.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'ourPrograms.html',{'programs':programs,'alert':alert,'captcha':captcha})
    return render(request,'ourPrograms.html',{'programs':programs,'captcha':captcha})