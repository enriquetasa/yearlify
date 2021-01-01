from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Letter
    )
from .forms import (
    LetterForm
    )

from accounts.models import User

import datetime

def explain(request):
    return render(request, 'explain.html', context={})

@login_required
def compose(request):
    form = LetterForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():

            due_date = datetime.date(2021, 12, 30)

            new_letter = Letter(
                user=request.user,
                content=form.cleaned_data['content'],
                send_on=due_date, 
            )
            new_letter.save()
            return redirect('letters:success')

    context = {
        'form': form
    }
    return render(request, 'compose.html', context=context)

@login_required
def success(request):
    return render(request, 'success.html', context={})

@login_required
def list_letters(request):
    letters = Letter.objects.filter(user=request.user).all()
    context = {
        'letters': letters
    }
    return render(request, 'list.html', context=context)
