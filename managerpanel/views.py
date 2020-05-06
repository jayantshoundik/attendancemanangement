from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminpanel.models import User,Attendance,Leavetype,Leave
import datetime
from project.decorators  import manager_required
from time import gmtime, strftime,strptime 
from django.http import JsonResponse
from adminpanel.forms import ApplyLeaveForm

# Create your views here.
def index(request):
    return render(request,'front/index.html')

@manager_required
def manageattendance(request):
    usermanager = User.objects.get(manager= request.user)
    manageattendance = Attendance.objects.filter(reference=usermanager)
    return render(request, 'front/manageattendance.html',{'manageattendances':manageattendance})

@manager_required
def manageleave(request):
    usermanager = User.objects.filter(manager= request.user)
    manageattendance = Leave.objects.filter(reference=usermanager)
    return render(request, 'front/manageattendance.html',{'manageattendances':manageattendance})
