from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users.forms import *


def register(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_detail')
    else:
        form = ProfileCreateForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def profile_detail(request):  
    return render(request, "users/profile_detail.html", {"user": request.user})

@login_required
def profile_change(request):
    if request.method == "POST":
        form = ProfileChangeForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect("profile_detail")
    else:
        form = ProfileChangeForm(instance=request.user)

    return render(
        request,
        "users/profile_change.html",
        {"form": form}
    )
