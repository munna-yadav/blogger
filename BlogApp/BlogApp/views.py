from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    return render(request,"layout.html")

def test(request):
    return render(request,'test.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegistrationForm  # Assuming you're using your custom form

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User creation successful. You are now logged in.")
            # login(request, user)
            return redirect('home')
        else:
            messages.error(request,"error")
    else:
          
        form = UserRegistrationForm()

    return render(request, 'registration.html', {"form": form})
