from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path('student_dashboard' , student_dashboard_view , name='student_dashboard' ), 
    path('student_login' , student_login , name='student_login' ), 
]
