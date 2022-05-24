from django.urls import path
from manohar_admin.views import *

urlpatterns = [
    path('',index_view),
    path('about/',about_view),
    path('contact/',contact_view),
    path('gallery/',gallery_view),
    path('mediacoverage/',mediaCoverage_view),
    path('overprog/',ourPrograms_view),
    path('ytlist/',youtubelist_view),
    path('join/',joinPage),
    path('temp/',temp)
]
