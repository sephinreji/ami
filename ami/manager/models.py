from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile_admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username

class Batch(models.Model):
    name=models.CharField(max_length=60)

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=60,null=True)
    address=models.CharField(max_length=255,null=True)
    phone=models.BigIntegerField(max_length=12,null=True,unique=True)
    email=models.EmailField(max_length=100,null=True,unique=True)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)



class TraineeProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100,default=None)
    address=models.CharField(max_length=250,default=None)
    age=models.DateField(default=None)
    phone = models.BigIntegerField(max_length=10,default=None,unique=True)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)

    image = models.ImageField(max_length=255,upload_to='profile_pic',default='images/profile.jpg',null=True)





class Training_dept_lists(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField(max_length=300)
    phone=models.BigIntegerField(max_length=12)
    email=models.EmailField(max_length=25)
    description=models.TextField(max_length=500)
