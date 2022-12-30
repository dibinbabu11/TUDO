from audioop import reverse
from pickle import NONE
from django.shortcuts import redirect, render
from django . http import HttpResponse
from django.urls import reverse_lazy
from .models import Task
from . forms import Todoform
from django . views.generic import ListView
from django. views .generic.detail import DetailView
from django .views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = "add.html"
    context_object_name= 'task1'

class TaskDetailView(DetailView):
    model = Task
    template_name = "detail.html"
    context_object_name= "task"
class TaskKUpdateView(UpdateView):
    model = Task
    template_name = "update.html"
    context_object_name="task"
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={"pk":self.object.id})
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url: reverse_lazy('cbvadd')



def add(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get("priority",'')
        date=request.POST.get("date",'')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'add.html',{'task1':task1})

def detail(request):
    task=Task.objects.all()
    return render(request,'detail.html',{'task':task})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request,"edit.html",{'f':f,'task':task})
