from django.shortcuts import render, redirect
from Artical.models import Product, Cartproducts, Buyer_Orders
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
import random
from itertools import chain

def index_page(request): # Отображение главной страницы
    return render(request, 'Artical/index.html')

def basket(request): # Отображение корзины
    ser = request.user.id
    Cart = Cartproducts.objects.filter(US = ser)
    Prod = Product.objects.all()
    BO = Buyer_Orders.objects.filter(User_id = ser)
    Number = int(len(Cart))
    ListProd = {
        'Prod':Prod,
        'Cart':Cart,
        'BO':BO,
        'Pi':1,
        'Number':Number,
    }
    return render(request, 'Artical/basket.html',  ListProd)
    

def ListProducts(request): # отображение страницы товаров
    news = Product.objects.all()
    List = {
        'news':news,
    }
    return render(request, 'Artical/List_of_product.html',List)


def company(request): 
    return render(request, 'Artical/About_company.html')

def Locl_GRM(request):
    news = Product.objects.filter(Categories = 3)
    return render(request, 'Artical/List_of_product.html',{'news':news})

def Locl_Fuel_tank(request):
    news = Product.objects.filter(Categories = 5)
    return render(request, 'Artical/List_of_product.html',{'news':news})

def Locl_spark_plug(request):
    news = Product.objects.filter(Categories = 1)
    return render(request, 'Artical/List_of_product.html',{'news':news})

def Locl_Air_filter(request):
    news = Product.objects.filter(Categories = 2)
    return render(request, 'Artical/List_of_product.html',{'news':news})

def Locl_Oil_filter(request):
    news = Product.objects.filter(Categories = 4)
    return render(request, 'Artical/List_of_product.html',{'news':news})

def issuelist(request): # функция для отображения страницы для выдачи 
    return render (request, 'Artical/Issue.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # получение имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполнение аутентификации
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'Artical/index.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Deleting_an_item(request, ID):
    person = Cartproducts.objects.get(id=ID)
    Ipers = person.products_id
    Del_item_add_backet(Ipers)
    person.delete()
    return redirect('baskK', permanent=True)

def add_to_backet(request, item_id):
    Reducing_the_quantity_of_goods(item_id)
    id = Product.objects.get(pk=item_id)
    Cartproducts.objects.create(US=request.user.id, products=id)
    return render(request, 'Artical/index.html')

def Reducing_the_quantity_of_goods(item_id):
    Q = Product.objects.get(pk=item_id)
    Qi = Q.Quantity
    Qi = int(Qi) - int(1)
    Q = Product.objects.filter(pk=item_id).update(Quantity = Qi)

def Del_item_add_backet(Ipers):
    Item = Product.objects.get(pk = Ipers)
    ItemQ = Item.Quantity
    ItemQ = int(ItemQ) + int(1)
    Item =  Product.objects.filter(pk=Ipers).update(Quantity = ItemQ)
    
def Random():
    Q1 = random.randint(0,100)
    Q2 = random.randint(0,100)
    Q3 = Q1 + Q2
    return Q3

def TEST(request):
    NO = Random()
    Cart = Cartproducts.objects.filter(US = request.user.id)
    user = request.user.id
    i = 0
    for I in Cart:
        N = Cart[i].products_id
        Prod = Cart[i].products
        i = i + 1
        Buyer_Orders.objects.create(Products=Prod, User_id=request.user.id, Order_number=NO)
    Cart.delete()
    return render(request, 'Artical/index.html')
        

def display_of_Orders(request):
    BO = Buyer_Orders.objects.filter(User_id = request.user.id)
    Prod = Product.objects.all()
    last_One = Buyer_Orders.objects.first()
    last_doua = Buyer_Orders.objects.last()
    if last_One != None:
        i = last_One.pk
    count = Buyer_Orders.objects.filter(User_id = request.user.id).count()
    if count > 0:
        i = i + 1
        Nom = Buyer_Orders.objects.filter(User_id = request.user.id, pk = i)
        O = str(Nom)
        X = -1
        Y = 0
        V = BO[Y].pk
        VO = Buyer_Orders.objects.filter(User_id = request.user.id, pk=V)
        for L in BO:
            if X < count:
                X = X + 1
            if BO[Y].Order_number != BO[X].Order_number:
                Y = X
                Ni = BO[X].pk
                N = Buyer_Orders.objects.filter(User_id = request.user.id, pk=Ni)
                VO = VO.union(N)
        Order_list = {
            'last_One':last_One,
            'BO':BO,
            'Prod':Prod,
            'last_doua':last_doua,
            'Nom':Nom,
            'I':0,
            'VO':VO,
        }
        return render(request, 'Artical/Orders.html', Order_list)
    if count <= 0:
        return render(request, 'Artical/Orders.html')


def TeSt(request, Nomer): # удаление заказа
    Ord_Del = Buyer_Orders.objects.filter(Order_number=Nomer)
    i = -1
    for I in Ord_Del:
        i = i + 1
        N = Ord_Del[i].Products_id
        Q = Product.objects.get(pk=N)
        Qi = Q.Quantity
        Qi = int(Qi) + int(1)
        Q = Product.objects.filter(pk=N).update(Quantity = Qi)
    Ord_Del.delete()
    return redirect('Orders')

def search(request):
    query = request.GET.get('orders_number')
    orders = Buyer_Orders.objects.filter(Order_number = query)
    Prod = Product.objects.all()
    count = Buyer_Orders.objects.filter(Order_number = query).count()
    x = count
    x = x - 1
    if count > 0:
        ldoua = orders[x]
    else:
        if count <= 0:
            ldoua = count = Buyer_Orders.objects.filter(Order_number = -1)
    out = {
        'orders':orders,
        'prod':Prod,
        'count':count,
        'ldoua':ldoua,
    }

    return render(request, 'Artical/Issueout.html', out)

def orddelite(request, Nomer):
    Ord_Del = Buyer_Orders.objects.filter(Order_number=Nomer)
    Ord_Del.delete()
    return render (request, 'Artical/index.html')

# Create your views here.
