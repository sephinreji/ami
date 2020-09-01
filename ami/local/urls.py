from django.contrib import admin
from django.urls import path
from . import views
from .views import Dashboard1, Training_list, DetailDept,Attendance

urlpatterns = [

    path('',Training_list.as_view(),name='trainerdashboard'),
    path('description/<pk>',DetailDept.as_view(),name='description_tr1'),
    path('attendance/',Attendance.as_view(),name='attendance_enroll')


]
