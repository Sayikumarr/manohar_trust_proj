from django.contrib import admin

# Register your models here.

from manohar_admin.models import FAQ, Contact, Gallery_pic, JoinMT, MediaPost, Poster,Event_Vol_Spon_Count,Eventschedule, Program, TeamMate, YoutubeVideo

# Register your models here.
admin.site.register(Poster)
admin.site.register(Event_Vol_Spon_Count)
admin.site.register(Eventschedule)
admin.site.register(Program)
admin.site.register(Gallery_pic)
admin.site.register(YoutubeVideo)
admin.site.register(TeamMate)
admin.site.register(MediaPost)
admin.site.register(Contact)
admin.site.register(FAQ)
admin.site.register(JoinMT)
