from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.contrib import messages

def home(request):
    return render(request,"layout.html")



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
    return render(request, 'logout.html')