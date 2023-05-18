from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

#the render method is used to render a html page
#the redirect method is used to redirect to a specific url
#render parameters are request and the html page to be rendered
# rendering parameters could contain a dictionary of variables to be used in the html page
#redirect parameters are the url to be redirected to
def home(request):
    return render(request, 'accounts/base.html')

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        print('form = ',form)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('signing_registration_app:home')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('signing_registration_app:home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('signing_registration_app:login')