from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from Artical.models import Product
from django.contrib import auth
from .models import Admin
from Artical.forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout

def show_category(request, products_id):

    ser = request.user.id
    Cart = Cartproducts.objects.filter(US = 'Admin')
    Prod = Product.objects.filter(id = products_id)
    ListProd = {
        'Prod':Prod,
        'Cart':Cart,
        'Pi':products_id,
    }
    return render(request, 'Artical/basket.html',  ListProd)


def Login(request): # Авторизация
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username = username, password = password)
            if user is not None:
                login(request, user=user)
                return redirect ('Home')
            return redirect ('Home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})


def AUT(request):
    return render(request, 'Artical/basket.html', )

# Create your views here.
