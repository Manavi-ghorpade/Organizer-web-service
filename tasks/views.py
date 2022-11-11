from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from tasks.models import Task,TaskCategory
from tasks.forms import TaskEntryForm
from django.contrib.auth.models import User
# Create your views here
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def tasks(request):
    if(request.method=="GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("/tasks/")
    else:
        table_data = Task.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'tasks/tasks.html', context)

@login_required(login_url='/login/')
def completed(request,id):
    if (request.method == "GET"):
        task = Task.objects.get(id=id)
        if (task.is_completed==False):
            task.is_completed=True;
        else:
            task.is_completed=False;
        task.save()
        return redirect("/tasks/")


@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = TaskEntryForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                category = add_form.cleaned_data["category"]
                user = User.objects.get(id=request.user.id)
                Task(user=user, description=description, category=category).save()
                return redirect("/tasks/")
            else:
                context = {
                "form_data": add_form
                }
                return render(request, 'tasks/add.html', context)
        else:
            return redirect("/tasks/")
    else:
        context = {
        "form_data": TaskEntryForm()
        }
        return render(request, 'tasks/add.html', context)


@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        task = Task.objects.get(id=id)
        form = TaskEntryForm(instance=task)
        context = {"form_data": form}
        return render(request, 'tasks/edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = TaskEntryForm(request.POST)
            if (form.is_valid()):
                task = form.save(commit=False)
                task.user = request.user
                task.id = id
                task.save()
                return redirect("/tasks/")
            else:
                context = {
                "form_data": form
                }
                return render(request, 'tasks/add.html', context)
        else:
            return redirect("/tasks/")
