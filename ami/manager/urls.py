from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .views import DashboardView, TraineeProfileView, Training_list, DetailDept, TraineeList, TraineeUpdate, \
    TraineeDelete, ProfileTrainee

urlpatterns = [

    path('dashboard/',DashboardView.as_view(),name='viewdashboard'),
    path('trainee/',views.traineeregister,name='trainee_register'),
    path('profile/',TraineeProfileView.as_view(),name='tr_profile'),
    path('list/',Training_list.as_view(),name='list_dept'),
    path('trainer/',views.trainer_register,name='trainer_register'),
    path('description/<pk>',DetailDept.as_view(),name='description'),
    path('traineelist/',TraineeList.as_view(),name='traineelist'),
    path('edittrainee/<int:pk>',TraineeUpdate.as_view(),name='traineeupdate'),
    path('deletetrainee/<int:pk>',TraineeDelete.as_view(),name='traineedelete'),
    path('profile/<int:pk>',ProfileTrainee.as_view(),name='traineeprofile')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)