from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from adminpanel.models import User,Attendance,Leavetype,Leave,Role
import datetime
from project.decorators  import manager_required
from time import gmtime, strftime,strptime 
from django.http import JsonResponse
from adminpanel.forms import ApplyLeaveForm,EmployeeForm,EditEmployeeForm
from django.template.loader import render_to_string

# Create your views here.
def dashboard(request):
    return render(request,'front/managerdashboard.html')

@manager_required
def manageattendance(request):
    usermanager = User.objects.get(manager= request.user)
    manageattendance = Attendance.objects.filter(reference=usermanager)
    return render(request, 'front/manageattendance.html',{'manageattendances':manageattendance})

@manager_required
def manageleave(request):
    appliedleaves = Leave.objects.filter(reference = request.user) 
    return render(request, 'front/manageleave.html', {'appliedleaves':appliedleaves})

@manager_required
def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
    else:
        form = EmployeeForm()
    return render(request, 'adminpanel/addemployee.html', {'form': form})

@manager_required
def employeeList(request):
    role = Role.objects.get(role='EMPLOYEE')
    employees = User.objects.filter(roles=role,manager= request.user)
    return render(request, 'adminpanel/employeelist.html', {'employees': employees})

@manager_required
def employeeEdit(request,pk):
    data = dict()
    employee = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save() 
            return redirect('employees')
    else:
        form = EditEmployeeForm(instance=employee)

    data['html_form'] = render_to_string('adminpanel/partial_employee_edit.html', {'form': form}, request=request)
    return JsonResponse(data)


@manager_required
def approvAttendance(request,pk):
    data = dict()
    attendancelist = get_object_or_404(Attendance, pk=pk)
    if attendancelist.status == 0:
        attendancelist.status = 1
    elif attendancelist.status == 1:
        attendancelist.status = 0
    attendancelist.save()
    return JsonResponse(data)

@manager_required
def approveLeave(request,pk):
    data = dict()
    attendancelist = get_object_or_404(Leave, pk=pk)
    if attendancelist.status == 0:
        attendancelist.status = 1
    elif attendancelist.status == 1:
        attendancelist.status = 0
    attendancelist.save()
    return JsonResponse(data)
