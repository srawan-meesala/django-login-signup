from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import AccountUserCreationForm
from django.template import loader

def home(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

class NewLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')

def signup(request):
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('signup successful')
            return redirect('dashboard')
    else:
        form = AccountUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    if request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html', {'user': request.user})
    elif request.user.user_type == 'patient':
        return render(request, 'patient_dashboard.html', {'user': request.user})
    return redirect('login')