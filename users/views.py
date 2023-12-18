from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    # if request is a POST, instantiate form data, else load form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # validate form data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('index')
    else:
        form = UserRegisterForm() 
    
    return render(request, 'users/register.html', {'form': form})