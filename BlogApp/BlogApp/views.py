from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.contrib import messages

def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,"blog/welcome.html")



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User creation successful. You are now logged in.")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"error")
    else:
          
        form = UserRegistrationForm()

    return render(request, 'registration.html', {"form": form})


def custom_logout(request):
    logout(request)
    return render(request, 'blog/welcome.html')