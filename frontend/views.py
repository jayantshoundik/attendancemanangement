from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminpanel.models import User,Attendance,Leavetype,Leave,Role,Department
import datetime
from project.decorators  import employee_required
from time import gmtime, strftime,strptime 
from django.http import JsonResponse
from adminpanel.forms import ApplyLeaveForm
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout,get_user_model


# Create your views here.
@employee_required
def index(request):
    return render(request,'front/index.html')

@employee_required
def attendance(request):
    userdetail = User.objects.get(username = request.user.username)
    attendancedate = datetime.date.today()
    usertodayattendance = Attendance.objects.filter(reference=request.user,attendancedate=attendancedate)
   
    if not usertodayattendance:
       usertodayattendance = usertodayattendance
    else:
        usertodayattendance = usertodayattendance[0]
    return render(request, 'front/attendance.html',{'usertodayattendance':usertodayattendance})

@employee_required
def attendancemark(request):
    data = dict()
    data['res'] =0
    userdetail = User.objects.get(username = request.user.username)
    attendancedate = datetime.date.today()
    
    if Attendance.objects.filter(reference=request.user,attendancedate=attendancedate).exists():
        usertodayattendance = Attendance.objects.get(reference=request.user,attendancedate=attendancedate)
        statuscheck = usertodayattendance.statustimein
        if statuscheck == 1:
                timeout = datetime.datetime.now().strftime('%H:%M:%S')
                statustimeout = 1
                usertodayattendance.statustimeout = statustimeout
                usertodayattendance.timeout = timeout
                usertodayattendance.save()
                print(usertodayattendance.timeout)
                data['res'] =1
                return JsonResponse(data)  
    else :
        timein = datetime.datetime.now().strftime('%H:%M:%S')
        statustimein = 1
        Attendance.objects.create(timein=timein, attendancedate=attendancedate,reference_id=userdetail.id,statustimein=statustimein)
        data['res'] =1
        return JsonResponse(data)   
    return JsonResponse(data)
@employee_required
def applyleave(request):
    if request.method == 'POST':
        form = ApplyLeaveForm(request.POST)
        if form.is_valid():
            leavestart = datetime.datetime.strptime(form.cleaned_data['leavestart'], '%Y-%m-%d')
            leaveend = datetime.datetime.strptime(form.cleaned_data['leaveend'], '%Y-%m-%d')
            obj = form.save(commit=False)
            obj.reference = request.user
            obj.leavestart = leavestart
            obj.leaveend = leaveend
            new = obj.save() 
            return HttpResponse(new)
    else:
        form = ApplyLeaveForm()
    appliedleaves = Leave.objects.filter(reference = request.user)
    return render(request, 'front/applyleave.html', {'form': form,'appliedleaves':appliedleaves})

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        
        if user is not None:
            auth_login(request, user)
            if user.roles_id == 1:
                return redirect('adminpanel/dashboard')
            elif user.roles_id == 2:
                return redirect('managerpanel/dashboard')
            elif user.roles_id == 3:
                return redirect('dashboard')
    
    return render(request,'adminpanel/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
