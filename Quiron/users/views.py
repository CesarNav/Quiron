""" Django modules """
from django.shortcuts import render, redirect
# Login and authenticate module
from django.contrib.auth import authenticate, login
# Login needed decorator
from django.contrib.auth.decorators import login_required
# Logout module
from django.contrib.auth import logout
# User cretion module
from django.contrib.auth.models import User
# Import profile user model
from users.models import Profile

""" Exceptions """
from django.db.utils import IntegrityError

""" Views """

""" Home view """
@login_required(login_url='/login/')
def home(request):
    return render(request,'baseh.html')

""" Profile view """
def user_profile(request):
    return render(request, 'profile.html')

def prof_update(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        prof_register = request.POST['prof_register']

        user = User()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.prof_register = request.POST['prof_register']
        user.save()

        return redirect('profile')
    return render(request,'prof_update.html')

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
            return render(request, 'login.html', {'errorlogin':'Usuario o contraseña invalida'})
    return render(request,'login.html')

""" Signin view """
def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_conf = request.POST['password_conf']
        # Password match test
        if password != password_conf:
            return render(request,'signin.html', {'errorsignin': 'Las contraseñas no coinciden'})

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        prof_register = request.POST['prof_register']
        
        # Create user with the fields above
        # Launch an exception when the username alredy exist 
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request,'signin.html', {'errorsignin': 'Nombre de usuario en uso'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.prof_register = request.POST['prof_register']
        user.save()
        
        # Create user profile
        profile = Profile(user=user)
        profile.prof_register = request.POST['prof_register']
        profile.save()

        # Redirect to login view
        return redirect('home')
    return render(request,'signin.html')

""" Logout view """
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')