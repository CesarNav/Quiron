""" Django modules """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

""" Home view """
@login_required(login_url='/login/')
def home(request):
    return render(request,'base.html')

""" Profole view """
def user_profile(request):
    return render(request, '')

""" Login view """
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            # Redirect to home view
            return redirect ('home')
        else:
            # Return a error message
            return render(request, 'login.html', {'error':'Usuario o contraseña invalida'})
    return render(request,'login.html')