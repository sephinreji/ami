from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
# Create your views here.
from .forms import TraineeRegisterForm, TraineeProfileForm, TrainerRegisterForm, TrainerProfileForm
from .models import TraineeProfile, Batch, Training_dept_lists, TrainerProfile
from .decorators import unauthenticated_user,allowed_users

@method_decorator(allowed_users(allowed_roles=['admin']),name='dispatch')
class DashboardView(LoginRequiredMixin,View):
    def get(self,request):
        count_one=TraineeProfile.objects.all().count()
        count_two=TrainerProfile.objects.all().count()

        return render(request,'manager/dashboard.html',{'count_one':count_one,'count_two':count_two})
@method_decorator(allowed_users(allowed_roles=['admin']),name='dispatch')
class TraineeRegisterView(LoginRequiredMixin,CreateView):
        model = User
        fields = ['username']

        template_name = 'manager/user_form.html'

def traineeregister(request):

    if request.method == 'POST':
        form = TraineeRegisterForm(request.POST)

        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name='trainee')
            print(group)
            user.groups.add(group)
            return redirect('tr_profile')
    else:
        form = TraineeRegisterForm()
    return render(request,'manager/user_form.html',{'form':form})

@method_decorator(allowed_users(allowed_roles=['admin']),name='dispatch')
class TraineeProfileView(LoginRequiredMixin,View):
    def get(self,request):
        batches=Batch.objects.all()
        return render(request, 'manager/trainee_profile.html',{'batches':batches})
    def post(self,request):
        batches = Batch.objects.all()
        id1 = User.objects.order_by('-id')[0]
        print('hai')

        form=TraineeProfileForm(request.POST)
        print(form)
        if form.is_valid():
            print('haijh')
            print(id1.id)
            form=form.save(commit=False)
            print(form.name)
            form.user=id1
            form.save()
            return render(request, 'manager/success.html', {'id': id,'form':form})
        else:
            return render(request,'manager/trainee_profile.html',{'form':form,'batches':batches})

class TrainerView(LoginRequiredMixin,View):
    def get(self,request):
        batches=Batch.objects.all()
        return render(request,'manager/trainer_profile.html',{'batches':batches})
    def post(self):
        pass

@method_decorator(allowed_users(allowed_roles=['admin']),name='dispatch')
def trainer_register(request):
    batches = Batch.objects.all()
    if request.method=='POST':


        user_form= TrainerRegisterForm(request.POST)
        profile_form=TrainerProfileForm(request.POST)


        print('hai')
        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            group = Group.objects.get(name='trainer')
            print(group)
            user.groups.add(group)
            profile=profile_form.save(commit=True)
            profile.user=user
            profile.save()
            return redirect('viewdashboard')
        else:
            messages.error(request,'Please Chec')
    else:

        user_form = TrainerRegisterForm()
        profile_form = TrainerProfileForm()
    return render(request,'manager/trainer_profile.html',{'user_form':user_form,'profile_form':profile_form,'batches':batches})

class Training_list(ListView):
    model = Training_dept_lists
    template_name = 'manager/institute_lists.html'
    context_object_name = 'lists'
    paginate_by = 3

class DetailDept(DetailView):
    model = Training_dept_lists
    template_name = 'manager/dept_description.html'

class TraineeList(ListView):
    model=TraineeProfile
    template_name = 'manager/trainee_list.html'


class TraineeUpdate(UpdateView):
    model=TraineeProfile
    fields = ['name','age','phone','address','batch']
    batches=Batch.objects.all()
    context_object_name = 'batches'
    #context_object_name = 'hi'
    template_name = 'manager/trainee_profile.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['batches']=Batch.objects.all()
        return context
    def get_success_url(self):
        return reverse('traineelist')

class TraineeDelete(DeleteView):
    model = TraineeProfile
    print('hai')
    template_name = "manager/traineeprofile_confirm_delete.html"
    success_url = '/'

class ProfileTrainee(DetailView):
    model=TraineeProfile
    template_name = 'manager/profile.html'

