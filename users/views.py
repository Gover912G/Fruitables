from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('index')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'registration/register_user.html', {'form':form})

def login_user(request):
    pass
    return render(request, login_user.html)
    
def logout_user(request):
    pass
    return render(request, logout_user.html)