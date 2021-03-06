"""unmasked_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from unmasked_proj import views

urlpatterns = [
#    path ('firebaseTest', views.firebaseTest, name='test2'),
    path ('', views.index, name='test'), #Testing
    path ('About.html', views.about, name= 'about'),
    path ('Add.html', views.add,name="add"),
    path ('AdminHome.html',views.adminHome, name= 'adminHome'),
    path ('alert.html',views.alert, name="alert"),
    path ('Contact.html',views.contact, name ='contact'),
    path ('GeneralQuestions.html',views.genQuestions, name="generalQuestions"),
    path ('Home.html', views.home, name='home'),
    path ('Login.html', views.login, name="login"),
    path ('Logout.html', views.logout, name='logout'),
    path ('ManageStudents.html', views.manageStudents, name="manageStudents"),
    path ('Support.html', views.support, name="support"),
    path ('Tips.html',views.tips,name='tips'),
]

urlpatterns+= static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)