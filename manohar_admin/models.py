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
    area = models.CharField(max_length=50,default='Event Area')
    details = models.CharField(max_length=300,default='Event Details')
    def __str__(self):
        return f'Event - {self.title}'

class Program(models.Model):
    title = models.CharField(max_length=50,default='Program Title')
    area = models.CharField(max_length=50,default='Program Area')
    details = models.CharField(max_length=500,default='Program Details')
    image = models.ImageField(default='default.png',upload_to='program_pics')
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

class MediaPost(models.Model):
    img = models.ImageField(default='default.png',upload_to='media_posts')

class Contact(models.Model):
    name = models.CharField(max_length=20,default='Name')
    email = models.CharField(max_length=50,default='Email')
    message = models.CharField(max_length=500,default='message')

class FAQ(models.Model):
    question = models.CharField(max_length=100,default='Question')
    answer = models.CharField(max_length=500,default='Answer')
