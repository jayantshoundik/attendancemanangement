from django.urls import path

from managerpanel import views

urlpatterns = [
     path('manageleave/',views.manageleave,name = 'manageleave'),
     path('manageattendance',views.manageattendance,name = 'manageattendance'),

]