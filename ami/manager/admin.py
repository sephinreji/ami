from django.contrib import admin
from .models import Training_dept_lists, Batch, TrainerProfile, TraineeProfile

# Register your models here.
admin.site.register(Training_dept_lists)
admin.site.register(Batch)
admin.site.register(TrainerProfile)
admin.site.register(TraineeProfile)