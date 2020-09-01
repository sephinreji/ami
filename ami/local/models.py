from django.db import models
from manager.models import TraineeProfile
# Create your models here.
class AttendanceModel(models.Model):
     trainee=models.ForeignKey(TraineeProfile,on_delete=models.CASCADE)
     name=models.CharField(max_length=100,null=True)
     date=models.DateField(null=True)
     timestamp=models.DateTimeField(auto_now=True,null=True)
     status=models.CharField(max_length=20,null=True)
     reason=models.CharField(max_length=255,null=True)

     def __str__(self):
          return self.name
