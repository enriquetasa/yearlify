from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import RegisterForm

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('letters:compose')
    else:
        form = RegisterForm(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context=context)
