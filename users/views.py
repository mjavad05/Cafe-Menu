from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RigesterUser
from django.contrib.auth import logout
import time
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RigesterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'wellcome {username}, successfully registered.')
            return redirect('login')
    else:
        form = RigesterUser()
    return render(request,'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    return render(request,'users/logout.html') 


@login_required
def profilepage(request):
    return render(request,'users/profile.html')