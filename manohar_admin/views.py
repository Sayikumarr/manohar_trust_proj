from django.shortcuts import render
from manohar_admin.forms import captchaForm
from manohar_admin.models import FAQ, Contact, Gallery_pic, JoinMT, MediaPost, Poster,Event_Vol_Spon_Count,Eventschedule, Program, TeamMate, YoutubeVideo
from django.conf import settings
from django.core.mail import send_mail

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
    pics = Gallery_pic.objects.all().order_by("-id")
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
    video = YoutubeVideo.objects.all().order_by("-id")
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
    mediaposts = MediaPost.objects.all().order_by("-id")
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
    programs = Program.objects.all().order_by("-id")
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

def joinPage(request):
    if request.method == 'POST':
        alert =[]
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        email=request.POST['email']
        phone=request.POST['phone']
        waphone=request.POST['waphone']
        bloodg=request.POST['bloodg']
        CAddress=request.POST['CAddress']
        PAddress=request.POST['PAddress']
        profession=request.POST['profession']
        serve=request.POST['serve']
        interested=request.POST['interested']
        skills=request.POST['skills']
        Message=request.POST['Message']
        if request.POST['Captcha']=='0110':
            subject = 'Your Details are submited Successfully @ ManoharTrust'
            message = f'''Hi {name}, Thank You for showing interest to join Our Manohar Trust Member... 
                             Name: {name}
                             Father Name: {fname}
                             Mother Name: {mname}
                             Email: {email}
                             Contact Number: {phone}
                             WhatsApp Number: {waphone}
                             Blood Group: {bloodg}
                             Present Address: {CAddress}
                             Permanent Adress: {PAddress}
                             Profession: {profession}
                             Serve: {serve}
                             Interested: {interested}
                             Skills: {skills}
                             Message: {Message}'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,'manoharsevasamithi@manohartrust.org', 'sayikumar@manohartrust.org',]
            send_mail( subject, message, email_from, recipient_list )
            newjoin = JoinMT(fullName = name,
                            fatherName = fname,
                            montherName = mname,
                            email = email,
                            conactNumber = phone,
                            whatsApp = waphone,
                            bloodGroup = bloodg,
                            presentAddress = CAddress,
                            permenantAddress = PAddress,
                            profession = profession,
                            willing_to_serve = serve,
                            interested = interested,
                            specialSkills = skills,
                            yourMessage = Message)
            newjoin.save()
            alert.append("SENT SUCCESSFULLY!")
        else:
            alert.append("Invalid  Captcha!")
        return render(request,'joinMTPage.html',{'alert':alert})
    return render(request,'joinMTPage.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def temp(request):
    if request.method == "POST":
        print(request.body)
        return render(request,'temp.html')
    return render(request,'temp.html')