from django.urls import path

from adminpanel import views

urlpatterns = [
     path('dashboard',views.index,name = 'dashboard'),
     path('employee/add',views.addEmployee,name = 'employeeadd'),
     path('employees',views.employeeList,name = 'employees'),
     path('employeeupdate/<int:pk>',views.employeeEdit,name = 'employeeupdate'),
     path('manager/add',views.addManager,name = 'manageradd'),
     path('managers',views.managerList,name = 'managers'),
     path('managerupdate/<int:pk>',views.managerEdit,name = 'managerupdate'),
     path('attendances',views.manageAttendance,name = 'attendances'),
     path('leaves',views.manageLeave,name = 'leaves'),
     path('leavetype/add',views.leaveType,name = 'leavetype'),
     path('leavetypeupdate/<int:pk>',views.leaveTypeEdit,name = 'leavetypeupdate'),
     path('approvedattendance/<int:pk>',views.approvAttendance,name = 'approvedattendance'),
     path('approvedleave/<int:pk>',views.approveLeave,name = 'approvedleave'),
     path('department',views.addDepartment,name = 'department'),

]