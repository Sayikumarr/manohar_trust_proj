from django.db import models
from datetime import datetime

# Create your models here.
class Poster(models.Model):
    image=models.ImageField(default='default.png',upload_to='poster_pics')
    title=models.CharField(max_length=50,default='POST Title')
    subtitle = models.CharField(max_length=150,default='here poster subtitle!')
    created=models.DateField(default=datetime.now)
    active=models.BooleanField(default=False)
    button_title = models.CharField(max_length=15,default='Click Here!')
    button_link = models.CharField(max_length=100,default='#')
    def __str__(self):
        return f'Poster - {self.title}'

class Event_Vol_Spon_Count(models.Model):
    events = models.PositiveBigIntegerField(default=0)
    volunteers = models.PositiveBigIntegerField(default=0)
    sponsers = models.PositiveBigIntegerField(default=0)

class Eventschedule(models.Model):
    title = models.CharField(max_length=50,default='Event Title')
    area = models.CharField(max_length=50,default='Event Area',null=True)
    details = models.CharField(max_length=300,default='Event Details')
    def __str__(self):
        return f'Event - {self.title}'

class Program(models.Model):
    title = models.CharField(max_length=50,default='Program Title')
    area = models.CharField(max_length=50,default='Program Area')
    details = models.TextField(max_length=1000,default='Program Details')
    
    titlecol = models.CharField(max_length=10,default='#000000')
    areacol = models.CharField(max_length=10,default='#000000')
    detailscol = models.CharField(max_length=10,default='#000000')

    image = models.ImageField(default='default.png',upload_to='program_pics')
    image_description = models.CharField(max_length=500,default='image description')
    def __str__(self):
        return f'Program - {self.title}'

class Gallery_pic(models.Model):
    img = models.ImageField(default='default.png',upload_to='gallery_pics')

class YoutubeVideo(models.Model):
    title = models.CharField(max_length=50,default='Video Title')
    link = models.CharField(max_length=100,default='Past Link Here')
    ytid = models.CharField(max_length=50,default='Dont Do anything here!')

    def save(self, *args, **kwargs):
        if self.ytid:
            if 'youtu.be' in self.link:
                i = self.link.find('e/')
                i+=2
                self.ytid = self.link[i:]
            else:
                i = self.link.find('v=')
                i+=2
                self.ytid = self.link[i:]
        super(YoutubeVideo, self).save(*args, **kwargs)

    def __str__(self):
        return f'Video - {self.title}'

class TeamMate(models.Model):
    name = models.CharField(max_length=20,default='Name')
    image = models.ImageField(default='default.png',upload_to='teammates_pics')
    position = models.CharField(max_length=15,default='position')
    email = models.CharField(max_length=50,default='Email')
    facebook = models.CharField(max_length=100,default='facebook-profile-link')
    twitter = models.CharField(max_length=100,default='twitter-profile-link')
    linkedin = models.CharField(max_length=100,default='linkedin-profile-link')
    def __str__(self):
        return f'Team Mate - {self.name}'

class MediaPost(models.Model):
    img = models.ImageField(default='default.png',upload_to='media_posts')

class Contact(models.Model):
    name = models.CharField(max_length=20,default='Name')
    email = models.CharField(max_length=50,default='Email')
    message = models.CharField(max_length=500,default='message')
    def __str__(self):
        return f'{self.email}'

class FAQ(models.Model):
    question = models.CharField(max_length=100,default='Question')
    answer = models.CharField(max_length=500,default='Answer')
    def __str__(self):
        return f'FAQ - {self.question}'


class JoinMT(models.Model):
    fullName = models.CharField(max_length=50,null=True)
    fatherName = models.CharField(max_length=50,null=True)
    montherName=models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    conactNumber = models.PositiveBigIntegerField(null=True)
    whatsApp = models.PositiveBigIntegerField(null=True)
    bloodGroup = models.CharField(max_length=4,choices=(
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ),null=True)
    presentAddress = models.TextField(max_length=250,null=True)
    permenantAddress = models.TextField(max_length=250,null=True)
    profession = models.CharField(max_length=75,null=True)
    willing_to_serve = models.CharField(max_length=12,choices=(
    ("Weekends", "Weekends"),
    ("Weekdays", "Weekdays"),
    ("AnyTime", "AnyTime"),
    ),null=True)
    interested = models.CharField(max_length=30,choices=(
    ("Social Media", "Social Media"),
    ("Marketing", "Marketing"),
    ("Web Design", "Web Design"),
    ("Fund Raising", "Fund Raising"),
    ("Data Entry", "Data Entry"),
    ("Poster Design", "Poster Design"),
    ('Training','Training'),
    ('Social Volunteering','Social Volunteering'),
    ('Event Planning and Managing','Event Planning and Managing'),
    ('Photography','Photography'),
    ('Videography','Videography'),
    ),null=True)
    specialSkills = models.CharField(max_length=100,null=True)
    yourMessage = models.TextField(max_length=500,null=True)
    def __str__(self):
        return f'Poster - {self.fullName}'
