"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from tasks import views as tasks_views
from budget import views as budget_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', tasks_views.tasks, name='task'),
    path('tasks/add/', tasks_views.add, name='task'),
    path('tasks/edit/<int:id>/', tasks_views.edit, name='task'),
    path('tasks/Completed/<int:id>/', tasks_views.completed, name='task'),
    path('budget/', budget_views.budget, name='budget'),
    path('budget/add/', budget_views.add, name='budget'),
    path('budget/edit/<int:id>/', budget_views.edit, name='budget'),
    path('', core_views.home, name='home'),
    path('about/', core_views.about),
    path('join/',core_views.join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),

]
