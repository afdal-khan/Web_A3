from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
import datetime

# Create your views here.
def home(request):
    date_now = datetime.datetime.now()
    day = date_now.strftime('%d-%m-%Y')
    time = date_now.strftime('%H:%M')

    args = {
        'date': day,
        'time':time
    }

    return render(request, 'accounts/home.html', args)

def register (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/listings')
    else:
        form = RegistrationForm()
    
    args = { 'form':form }
    return render(request, 'accounts/reg_form.html', args)


    