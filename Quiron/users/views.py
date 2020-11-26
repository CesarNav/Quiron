from django.shortcuts import render


def user_home(request):
    return render(request,'base.html')

def user_profile(request):
    return render(request, '')