from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import TraineeProfile, TrainerProfile


class TraineeRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username','email','password1','password2']

class TraineeProfileForm(forms.ModelForm):
    image=forms.ImageField(required=False)
    class Meta():
        model=TraineeProfile
        fields=['name','age','phone','address','batch','image']


class TrainerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username','email','password1','password2']


class TrainerProfileForm(forms.ModelForm):

    class Meta():
        model=TrainerProfile

        fields=['name','email','phone','address','batch']
