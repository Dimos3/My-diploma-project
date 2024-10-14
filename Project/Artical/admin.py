from django.contrib import admin
from .models import Product
from .models import Cartproducts
from .models import Category
from .models import Buyer_Orders

admin.site.register(Product)
admin.site.register(Cartproducts)
admin.site.register(Category)
admin.site.register(Buyer_Orders)


# Register your models here.
