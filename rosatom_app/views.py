from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Task, UsefulMaterial
from .forms import TaskForm, AddUsefulForm


def index(request):
    return redirect('rosatom_app:home')

@login_required(login_url='rosatom_users:login')
def home(request):
    try:
        # Current user is novice

        novice = request.user.novice
        context = {}
        context['name'] = novice.fullname.split()[1]
        context['department'] = novice.department
        context['position'] = novice.position
        context['salary'] = novice.salary
        context['schedule'] = novice.schedule.strip().split('\n')
        context['workplace'] = novice.workplace
        context['number_of_tasks'] = len(Task.objects.filter(novice=novice.id))
        context['tasks'] = list(Task.objects.filter(novice=novice.id))
        context['mentor'] = novice.mentor

        return render(request, 'rosatom_app/home_novice.html', context)

    except AttributeError:
        try:
            # Current user is Mentor

            mentor = request.user.mentor
            novice = mentor.novice
            context = {}
            context['name'] = mentor.fullname.split()[1]
            context['department'] = mentor.department
            context['tasks'] = [(task, task.deadline.strftime("%Y-%m-%dT%H:%M"))
                                for task in Task.objects.filter(novice=novice.id)]
            context['number_of_tasks'] = len(Task.objects.filter(novice=novice.id))
            
            context['novice'] = novice
            form = TaskForm()
            context['form'] = form
            
            return render(request, 'rosatom_app/home_mentor.html', context)
        except AttributeError:
            return render(request, 'errors/404.html')


@login_required(login_url='rosatom_users:login')
def edit_task(request):
    task_inst = get_object_or_404(Task, pk=request.POST['task_id'])
    
    task_name = request.POST.get('task_name')
    deadline = datetime.strptime(request.POST.get('deadline'), "%Y-%m-%dT%H:%M")

    content = request.POST.get('content')

    try:
        task_inst.task_name = task_name
        task_inst.content = content
        task_inst.deadline = deadline   
        task_inst.save()
        return redirect('rosatom_app:home')
    except:
        render(request, 'errors/404.html')


@login_required(login_url='rosatom_users:login')
def add_task(request):
    novice = request.user.mentor.novice
    form = TaskForm(data=request.POST)
    try:  
        new_task = form.save(commit=False)
        new_task.novice = novice
        new_task.save()
        return redirect('rosatom_app:home')
    except:
        render(request, 'errors/404.html')


@login_required(login_url='rosatom_users:login')
def useful(request):
    context = {}
    try:
        user = request.user.novice
    except AttributeError:
        user = request.user.mentor
        context['can_edit'] = True
        context['form'] = AddUsefulForm
    
    ums = list(UsefulMaterial.objects.filter(department=user.department))
    context['useful_materials'] = ums
    context['name'] = user.fullname.split()[1]
    
    return render(request, 'rosatom_app/useful.html', context)


@login_required(login_url='rosatom_users:login')
def add_useful(request):
    form = AddUsefulForm(data=request.POST)

    if form.is_valid():
        um = form.save(commit=False)
        um.department = request.user.mentor.department
        um.save()
        return redirect('rosatom_app:useful')

@login_required(login_url='rosatom_users:login')
def collective(request):
    return render(request, 'rosatom_app/collective.html')