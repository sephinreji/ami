from django.contrib.auth.forms import UserCreationForm
from django import forms, dispatch
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.views.generic import CreateView
from .decorators import unauthenticated_user

class IndexView(View):
    def get(self,request):
        return render(request, 'users/index.html')

class AboutView(View):
    def get(self,request):
        return render(request,'users/about.html')

@method_decorator(unauthenticated_user,name='dispatch')
class LoginView(View):
    def post(self,request):

        print('hai')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print('woow',user)
        if user is not None:
            if user.groups.filter(name='admin').exists():
                print(username, password)
                login(request, user)
                print('iam admin')
                messages.success(request, 'Welcome')
                return redirect('viewdashboard')
            elif user.groups.filter(name='trainer').exists():
                print(username, password)
                login(request, user)
                print('iam trainer')
                messages.success(request, 'Welcome')
                return redirect('trainerdashboard')

        else:
            raise Http404("User doesnot exist")


    def get(self,request):
        print('hai')
        return render(request, template_name='users/login.html')

class LogoutView(View):
     def get(self,request):
         logout(request)
         return redirect('index')


class TraineeRegisterView(CreateView):
    model = User
    fields = ['email','username', 'password1', 'password2']
