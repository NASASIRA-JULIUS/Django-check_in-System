from django.db.models import fields
from django.forms.models import fields_for_model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import visitor
from .form import VisitorForm, CreateUserForm
from django import forms
from .filter import VisitorFilter
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users,admin_only
from django.contrib.auth.models import Group


# Create your views here.
@login_required(login_url='login')

def home(request):
    home=visitor.objects.all()
    return render(request,'checkin/home.html',{'home':home})


@login_required(login_url='login')

def users(request):
    users=visitor.objects.all()
    total_users=users.count()
    myFilter=VisitorFilter(request.GET, queryset=users)
    users=myFilter.qs

    context={'users':users,'total_users':total_users,'myFilter':myFilter}
    return render(request, 'checkin/users.html',context)


@login_required(login_url='login')
def register(request):
    form=VisitorForm()
    if request.method == 'POST':
        form =VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users') 
    context={'form':form}
    return render(request, 'checkin/register.html',context)

@login_required(login_url='login')

def update_user(request, pk):
    user=visitor.objects.get(id=pk)
    form=VisitorForm(instance=user)
    if request.method == 'POST':
        form =VisitorForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')


    context={'form':form}
    return render(request, 'checkin/register.html',context)


@login_required(login_url='login')

def delete_user(request, pk):
    user=visitor.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        return redirect('users')

    context={'item':user}
    return render(request, 'checkin/delete.html',context)






@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='tenants/visitors')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'checkin/registerPage.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'checkin/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def userPage(request):
	
	context = {}
	return render(request, 'checkin/user.html', context)
	