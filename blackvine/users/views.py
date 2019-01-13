from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import CustomerForm

def customer_new(request, template='users/user_new.html'):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last-name']

            #THIS CREATE USER RECORD AND SAVE IT TO DATA BASE
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('')
    else:
        form = CustomerForm()

    return render(request, template, {'form': form})
