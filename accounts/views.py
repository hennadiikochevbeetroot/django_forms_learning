from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:main_menu')
    else:
        form = UserCreationForm()

    return render(request, template_name='accounts/register.html', context={'form': form})
