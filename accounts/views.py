from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Account created successfully!')
            return redirect('recipes:main_menu')  # Redirect to homepage or some other page after registration
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})