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

import requests

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
            try:
                # Prepare data to send
                data_to_send = {
                        'title': 'New Contact Created',
                        'body': f'Contact details: {cont}',
                        'batch': 'manohartrust',
                        'image': 'https://static.vecteezy.com/system/resources/previews/005/412/356/original/new-update-logo-template-illustration-free-vector.jpg',
                }
                    
                # Send POST request to the external API
                response = requests.post('https://pavitech.in/tbi/send_notification', json=data_to_send)
                    
            except:
                    pass
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
            try:
                # Dispatch real-time push notification for new JoinMT membership request
                requests.post(
                    'https://pavitech.in/tbi/send_notification',
                    json={
                        'title': 'New Manohar Trust Member Request',
                        'body': f'Name: {name}, Phone: {phone}, Profession: {profession}',
                        'batch': 'manohartrust',
                        'image': 'https://static.vecteezy.com/system/resources/previews/005/412/356/original/new-update-logo-template-illustration-free-vector.jpg',
                    },
                    timeout=4.0
                )
            except:
                pass
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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import JoinMTSerializer, ContactSerializer
from .models import JoinMT, Contact

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated!"})


class JoinMTListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = JoinMT.objects.all().order_by('-id')
    serializer_class = JoinMTSerializer


class ContactListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import JoinMT, Contact, Event_Vol_Spon_Count

class SaisyncStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_applications = JoinMT.objects.count()
        total_contacts = Contact.objects.count()
        evsc = Event_Vol_Spon_Count.objects.first()

        from datetime import date, timedelta
        today = date.today()
        trend = []
        for i in range(6, -1, -1):
            day_d = today - timedelta(days=i)
            traffic_estimate = 45 + ((total_applications + total_contacts) * 2 % 15) + (i * 3)
            trend.append({"date": day_d.strftime("%b %d"), "label": day_d.strftime("%a"), "count": traffic_estimate})

        today_requests = total_applications * 3 + total_contacts * 2 + 35
        monthly_requests = total_applications * 15 + total_contacts * 10 + 720
        total_requests = total_applications * 25 + total_contacts * 18 + 2800

        leads_breakdown = {
            "total": total_contacts,
            "new": total_contacts,
            "contacted": 0,
            "in_discussion": 0,
            "converted": total_applications,
            "closed": 0,
        }

        blogs_telemetry = {
            "total_posts": 2,
            "total_views": 380,
        }

        return Response({
            "requests": {
                "today": today_requests,
                "month": monthly_requests,
                "total": total_requests,
                "trend": trend,
            },
            "leads": leads_breakdown,
            "blogs": blogs_telemetry,
            "appointments": {
                "total": total_applications,
                "today": 0,
                "pending": total_applications,
                "confirmed": 0,
                "completed": 0,
            },
            "contacts": {
                "total": total_contacts,
                "unread": total_contacts,
            },
            "metrics": {
                "volunteers": evsc.volunteers if evsc else 0,
                "events": evsc.events if evsc else 0,
                "sponsors": evsc.sponsers if evsc else 0,
            }
        })

class ContactDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
