from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('grocery:index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register_user.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, 'grocery:index')
    else:
        form = LoginForm()
    return render(request, 'registration/login_user.html', {'form':form})
    
def logout_user(request):
    logout(request)
    return redirect('users:login')