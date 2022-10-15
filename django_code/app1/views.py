import email
from email import message
from multiprocessing import context
import re
from tkinter import Variable
from unicodedata import name
from django.shortcuts import render,HttpResponse

from app1.models import Contact
from datetime import datetime
from app1.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    """context={
        "variable1":"  yo brooo",
        "variable2":"  hello guyzz"
    }"""

    #messages.success(request, "submited sucssafully")

    return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def services(request):
    return render(request,'sevices.html')
    #return HttpResponse("this is about services")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('phone')
        contact = Contact(name= name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent successcfully.')

    return render(request,'contact.html')
   # return HttpResponse("this is contact page")    

def s1(request):
    return render(request,'s1.html')
    #return HttpResponse("this is contact page")    

def s2(request):
    return render(request,'s2.html')