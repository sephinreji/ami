from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView, CreateView

from manager.models import Training_dept_lists,TraineeProfile,TrainerProfile

from .forms import AttendanceForm
from .models import AttendanceModel
from django.forms import formset_factory




class Dashboard1(View):
    def get(self,request):
        return render(request,template_name='local/trainer_dashboard.html')

class Attendance(View):
    def get(self,request):
        trainer=request.user.id
        print(trainer)
        tr=TrainerProfile.objects.get(user_id=trainer)
        batch=tr.batch
        print(batch.id)
        trainee=TraineeProfile.objects.filter(batch=batch)

        return render(request,'local/attendance.html',{'formset':trainee})
    def post(self,request):
        f=AttendanceForm(request.POST)
        print(f)
        traineelist=request.POST.getlist('trainee')
        namelist=request.POST.getlist('name')
        date=request.POST.getlist('date')
        statuslist=request.POST.getlist('status')
        reasonlist=request.POST.getlist('reason')
        print(traineelist,namelist,date,statuslist,reasonlist)

        for i in range(len(traineelist)):
            trainee =TraineeProfile.objects.get(id=traineelist[i])
            print(trainee)
            name=namelist[i]
            date1=date[0]
            print(date1)
            status=statuslist[i]
            reason=reasonlist[i]
            print('woww',trainee,type(name),type(reason),type(status),type(date))
            dict={'trainee':trainee,
                  'name':name,
                  'date':date1,
                  'status':status,
                  'reason':reason}
            print(dict)
            AttendanceModel.objects.create(trainee=trainee,name=name,date=date1,status=status,reason=reason)










class Training_list(ListView):
    model = Training_dept_lists
    template_name = 'local/institute_lists.html'
    context_object_name = 'lists'
    paginate_by = 3

class DetailDept(DetailView):
    model = Training_dept_lists
    template_name = 'local/dept_description.html'