from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            display_name = form.cleaned_data.get('display_name')
            user.display_name = display_name  # Directly set the display_name
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    return render(request, 'registration/login.html')
