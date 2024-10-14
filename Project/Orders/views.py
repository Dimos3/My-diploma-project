from django.shortcuts import render
from Artical.models import Buyer_Orders, Cartproducts 
import random

def Create_an_order(request, user_id):
    Cart = Cartproducts.objects.filter(US=user_id)
    C = Cart.products
    On =  randint(0, 10000)
    print(On)
    Buyer_Orders.objects.create(Products= C, User_id =request.user.id , Order_number = On )
# Create your views here.
