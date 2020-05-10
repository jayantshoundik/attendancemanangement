from django.urls import path

from frontend import views

urlpatterns = [
     path('',views.index,name = 'dashboard'),
     path('dashboard',views.index,name = 'dashboard'),
     path('login',views.login,name = 'login'),
     path('logout',views.logout,name = 'logout'),
     path('attendance/',views.attendance,name = 'attendance'),
     path('attendancemark/',views.attendancemark,name = 'attendancemark'),
     path('applyleave/',views.applyleave,name = 'applyleave'),
     path('attendancereport/',views.attendancereport,name = 'attendancereport'),
     path('leavereport/',views.leavereport,name = 'leavereport'),
     path('calender/',views.calender,name = 'calender'),
     
]