from django.urls import path

from managerpanel import views


urlpatterns = [
     path('manageleave/',views.manageleave,name = 'manageleave'),
     path('manageattendance',views.manageattendance,name = 'manageattendance'),
     path('dashboard',views.dashboard,name = 'dashboard'),
     path('employee/add',views.addEmployee,name = 'employeeadd'),
     path('employees',views.employeeList,name = 'employees'),
     path('employeeupdate/<int:pk>',views.employeeEdit,name = 'employeeupdate'),
     path('approvedattendance/<int:pk>',views.approvAttendance,name = 'approvedattendance'),
     path('approvedleave/<int:pk>',views.approveLeave,name = 'approvedleave'),
     path('managercalender/',views.calender,name = 'managercalender'),

]