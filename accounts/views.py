

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html') 
