from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.forms import JoinForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from tasks.models import Task
from budget.models import Budget
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def user_logout(request):
 	# Log out the user.
 	logout(request)
 	# Return to homepage.
 	return redirect("/")

def user_login(request):
 	if (request.method == 'POST'):
 		login_form = LoginForm(request.POST)
 		if login_form.is_valid():
 			# First get the username and password supplied
 			username = login_form.cleaned_data["username"]
 			password = login_form.cleaned_data["password"]
 			# Django's built-in authentication function:
 			user = authenticate(username=username, password=password)
 			# If we have a user
 			if user:
 				#Check it the account is active
 				if user.is_active:
 					# Log the user in.
 					login(request,user)
 					# Send the user back to homepage
 					return redirect("/")
 				else:
 				#	 If account is not active:
 					return HttpResponse("Your account is not active.")
 			else:
 				print("Someone tried to login and failed.")
 				print("They used username: {} and password: {}".format(username,password))
 				return render(request, 'core/login.html', {"login_form": LoginForm})
 	else:
			# return HttpResponse("Your account is not active.")
 			return render(request, 'core/login.html', {"login_form": LoginForm})


def join(request):
 	if (request.method == "POST"):
 		join_form = JoinForm(request.POST)
 		if (join_form.is_valid()):
	 		# Save form data to DB
	 		user = join_form.save()
	 		# Encrypt the password
	 		user.set_password(user.password)
	 		# Save encrypted password to DB
	 		user.save()
	 		# Success! Redirect to home page.
	 		return redirect("/login")
 		else:
	 		# Form invalid, print errors to console
	 		page_data = { "join_form": join_form }
	 		return render(request, 'core/join.html', page_data)
 	else:
 		join_form = JoinForm()
 		page_data = { "join_form": join_form }
 		return render(request, 'core/join.html', page_data)

def about(request):
	return render(request,'core/about.html')

# @login_required(login_url='/login/')
# def home(request):
# 	return render(request,'core/home.html')


@login_required(login_url='/login/')
def home(request):
    data=[]
    a=0
    b=0
    l=0
    k=0
    queryset = Task.objects.filter(user=request.user)
    for i in queryset:
        if(i.is_completed==False):
            a+=1
        else:
            b+=1
        l+=1
    data.append(b)
    data.append(a)

    projected=[]
    actual=[]
    values = Budget.objects.filter(user=request.user)
    for j in values:
        projected.append(j.projected)
        actual.append(j.actual)
        k+=1
    if(l!=0 and k!=0):
        context = {
            "series": data,
            "projected":projected,
            "actual":actual
            }
    elif(l == 0):
        context = {
            "series": 0,
            "projected":projected,
            "actual":actual
            }
    elif(k==0):
        context = {
            "series": data,
            "projected":0,
            "actual":0
        }
    else:
        context = {
            "series": 0,
            "projected":0,
            "actual":0
        }
    return render(request, "core/home.html",context)
