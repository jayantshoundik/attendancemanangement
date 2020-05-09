from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from project.decorators  import admin_required
from django.contrib.auth import login as auth_login, authenticate,logout as auth_logout,get_user_model
from adminpanel.models import User,Department,Leavetype,Role,Attendance,Leave

from adminpanel.forms import EmployeeForm,DepartmentForm,ManagerForm,LeaveTypeForm,EditEmployeeForm,EditManagerForm
from django.template.loader import render_to_string

# Create your views here.

@admin_required
def index(request):
    return render(request,'adminpanel/index.html')
@admin_required
def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
    else:
        form = EmployeeForm()
    return render(request, 'front/addemployee.html', {'form': form})

@admin_required
def employeeList(request):
    role = Role.objects.get(role='EMPLOYEE')
    employees = User.objects.filter(roles=role)
    return render(request, 'front/employeelist.html', {'employees': employees})
@admin_required
def calender(request):
    all_events = User.objects.filter(roles_id = 3)
    
    return render(request, 'front/calender.html',{'events':all_events})

@admin_required
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

@admin_required
def approvAttendance(request,pk):
    data = dict()
    attendancelist = get_object_or_404(Attendance, pk=pk)
    if attendancelist.status == 0:
        attendancelist.status = 1
    elif attendancelist.status == 1:
        attendancelist.status = 0
    attendancelist.save()
    return JsonResponse(data)

@admin_required
def approveLeave(request,pk):
    data = dict()
    attendancelist = get_object_or_404(Leave, pk=pk)
    if attendancelist.status == 0:
        attendancelist.status = 1
    elif attendancelist.status == 1:
        attendancelist.status = 0
    attendancelist.save()
    return JsonResponse(data)

@admin_required
def managerEdit(request,pk):
    data = dict()
    employee = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditManagerForm(request.POST, instance=employee)
        if form.is_valid():
            form.save() 
        return redirect('managers')
    else:
        form = EditManagerForm(instance=employee)

    data['html_form'] = render_to_string('adminpanel/partial_manager_edit.html', {'form': form}, request=request)
    return JsonResponse(data)


@admin_required
def addManager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
    else:
        form = ManagerForm()
    return render(request, 'adminpanel/addmanager.html', {'form': form})

@admin_required
def managerList(request):
    role = Role.objects.get(role='MANAGER')
    employees = User.objects.filter(roles=role)
    return render(request, 'adminpanel/managerlist.html', {'employees': employees})


@admin_required
def addDepartment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = DepartmentForm()
    departments = Department.objects.all() 
    return render(request, 'adminpanel/department.html', {'form': form,'departments':departments})


@admin_required
def leaveType(request):
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = LeaveTypeForm()
    leavetypes = Leavetype.objects.all() 
    return render(request, 'adminpanel/leavetype.html', {'form': form,'leavetypes':leavetypes})

@admin_required
def leaveTypeEdit(request,pk):
    data = dict()
    leavetype = get_object_or_404(Leavetype, pk=pk)
    if request.method == 'POST':
        form = LeaveTypeForm(request.POST, instance=leavetype)
        if form.is_valid():
            form.save() 
            return redirect('leavetype')
    else:
        form = LeaveTypeForm(instance=leavetype)

    data['html_form'] = render_to_string('adminpanel/partial_leavetype_edit.html', {'form': form}, request=request)
    return JsonResponse(data)

@admin_required
def manageAttendance(request):
    
    manageattendances = Attendance.objects.all() 
    return render(request, 'adminpanel/attendances.html', {'manageattendances':manageattendances})
@admin_required
def manageLeave(request):
    appliedleaves = Leave.objects.all() 
    return render(request, 'adminpanel/leaves.html', {'appliedleaves':appliedleaves})




