from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def register(request):
    form = RegisterForm(request.POST)
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
        else:
            form = RegisterForm()
    else:
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request, 'user_registration/register.html', context)

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            if user.is_active:
                auth.login(request,user) 
                messages.success(request, 'Login Successful')
                return redirect('admin_dashboard-page')
            else:
                messages.error(request, 'Account is not active')
                return render(request, 'user_registration/login.html')

        elif user is not None and not user.is_staff:
            if user.is_active:
                auth.login(request,user)
                messages.success(request, 'Login Successful')
                return redirect('staff_dashboard-page')
            else:
                messages.warning(request, 'Account is not active')
                return render(request, 'user_registration/login.html')
        else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'user_registration/login.html')

    return render(request, 'user_registration/login.html')

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('login-page')