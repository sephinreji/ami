from django import forms
from django.forms import modelformset_factory

from .models import AttendanceModel


class AttendanceForm(forms.ModelForm):
    class Meta():
        model=AttendanceModel
        fields=['trainee','name','status','date','reason']



