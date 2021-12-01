from django.shortcuts import render, redirect#will render/show web files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect  
from django.conf import settings
import pyrebase 
import firebase_admin
#from Cryptodome.Cypher import aes

#firebase class
class FireBase:
    def __init__(self):
        self.config = {
            "apiKey": "AIzaSyAxV8-iToKuLitUmG48EEkIddvq7iYrN2Y",
            "authDomain": "facial-recongition-38069.firebaseapp.com",
            "databaseURL": "https://facial-recongition-38069-default-rtdb.firebaseio.com",
            "projectId": "facial-recongition-38069",
            "storageBucket": "facial-recongition-38069.appspot.com",
            "messagingSenderId": "937313859878",
            "appId": "1:937313859878:web:25d017bad4c1df1255e9e7"
        }
        self.cred_obj = firebase_admin.credentials.Certificate(
            'C:/Users/rrrsy/Desktop/GitRipo/FacialRecognition/facial-recongition-38069-firebase-adminsdk.json')
        self.default_app = firebase_admin.initialize_app(
            self.cred_obj, {'databaseURL': self.config["databaseURL"]})
        firebase=pyrebase.initialize_app(self.config)
        authe = firebase.auth()
        database=firebase.database()
        
        #def firebaseTest(request):
        #    name = database.child("users").child("GTest").childe("email").get.val()
        #    return HttpResponse(name)

#Renders all webpages
def index (request):
    return HttpResponse("Hello, welcome to the index page.This is a test.")
def about (request):
    return render(request,'About.html')
def add(request):
    return render(request, 'Add.html')
def adminHome(request):
    return render(request, 'AdminHome.html')
def alert(request):
    return render(request, 'alert.html')
def contact(request):
    return render(request, 'Contact.html')
def genQuestions(request):
    return render(request, 'GeneralQuestions.html')
def home(request):
    return render(request, 'Home.html')
def login(request):
    return render(request, 'Login.html')
def logout(request):
    return render(request, 'LogoutPage.html')
def manageStudents(request):
    return render(request, 'ManageStudents.html')
def support(request):
    return render(request, 'Support.html')
def tips(request):
    return render(request, 'Tips.html')

