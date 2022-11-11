from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from budget.models import Budget,BudgetCategory
from budget.forms import BudgetEntryForm
from django.contrib.auth.models import User
# Create your views here
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def budget(request):
    if(request.method=="GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Budget.objects.filter(id=id).delete()
        return redirect("/budget/")
    else:
        table_data = Budget.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'budget/budget.html', context)

@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = BudgetEntryForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                category = add_form.cleaned_data["category"]
                actual = add_form.cleaned_data["actual"]
                projected = add_form.cleaned_data["projected"]
                user = User.objects.get(id=request.user.id)
                Budget(user=user, description=description, category=category, actual=actual, projected=projected).save()
                return redirect("/budget/")
            else:
                context = {
                "form_data": add_form
                }
                return render(request, 'budget/add.html', context)
        else:
            return redirect("/budget/")
    else:
        context = {
        "form_data": BudgetEntryForm()
        }
        return render(request, 'budget/add.html', context)


@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        budget = Budget.objects.get(id=id)
        form = BudgetEntryForm(instance=budget)
        context = {"form_data": form}
        return render(request, 'budget/edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = BudgetEntryForm(request.POST)
            if (form.is_valid()):
                budget = form.save(commit=False)
                budget.user = request.user
                budget.id = id
                budget.save()
                return redirect("/budget/")
            else:
                context = {
                "form_data": form
                }
                return render(request, 'budget/add.html', context)
        else:
            return redirect("/budget/")
