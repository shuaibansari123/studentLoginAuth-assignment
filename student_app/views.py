from django.shortcuts import render , redirect
from .models import Student
from django.contrib.auth import authenticate , login
from django.http import HttpResponse
# Create your views here.
import datetime
#from django.db.models import F , Q

# we can create class based and function based both views 
# i m creating func based for simplicity
# we can create custom auth backend also


def student_dashboard_view(request):
    #objs = Student.objects.annotate(age = F('date_of_birth__year') - datetime.year ).all() 
    # we can use only() , defer()
    # we can use request.user.is_authenticated or @login_required
    if request.user.is_authenticated:
        objs = Student.objects.all()
        return render(request , 'student_dashboard.html' , {'objs' : objs})
    return render(request , 'login_page.html' , {'msg' : 'please login first to see student data'})


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('my_password')
        # we can check if student_type == 'staff' or 'student' then only show the student details 
        user = authenticate(request , email=email  , password = password)
        print('user , = ' , user , email , password)
        if user is not None:

            login(request , user)
            print('login success')
            return redirect('student_dashboard')

        # obj = Student.objects.get(email=email)
        # if obj.check_password(password):
        #     login(request , obj)
        #     print('login success')
        #     return redirect('student_dashboard')
        else:
            print('login failed..')
            return render(request , 'login_failed.html' , {})
    return render(request , 'login_page.html')


