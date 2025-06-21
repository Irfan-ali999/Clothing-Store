# myapp/models.py
from django.db import models
from django.shortcuts import render , get_object_or_404,redirect
from .models import Product
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, RegistrationForm

# def home(request):
#     return HttpResponse("Hello, Django!")


def home(request):
    context = {'name': 'Irfan Ali'}
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'products/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'products/products.html', {'products': products})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage or dashboard
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




