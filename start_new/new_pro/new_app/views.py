from django.shortcuts import render
from .models import *
from django.http import *
from django.shortcuts import render, redirect
from .forms import RegisterForm


def home(request):
    obj = student.objects.all()
    return render(request, 'index.html', {'obj': obj})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})