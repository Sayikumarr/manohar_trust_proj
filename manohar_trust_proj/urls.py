"""manohar_trust_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

from rest_framework.authtoken.views import obtain_auth_token
from manohar_admin.views import ProtectedView, JoinMTListAPIView, ContactListAPIView


admin.site.site_header = "Manohar Trust Admin"
admin.site.site_title = "Manohar Trust Admin Portal"
admin.site.index_title = "Welcome to Manohar Trust Dashboard"

urlpatterns = [
    path('admin-portal/', admin.site.urls),
    path('',include('manohar_admin.urls')),
    path('captcha',include("captcha.urls")),
    path('saisync/token/', obtain_auth_token, name='api_token_auth'),
    path('saisync/protected/', ProtectedView.as_view(), name='protected_view'),
    path('saisync/appointments/', JoinMTListAPIView.as_view(), name='appointment_view'),
    path('saisync/contacts/', ContactListAPIView.as_view(), name='contact_view'),
]


if True:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)