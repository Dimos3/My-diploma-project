from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    Product_Name = models.CharField('Название', max_length=150)
    Categories = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name = 'Категория')
    Description = models.TextField('Описание')
    Quantity = models.CharField('Количество', max_length=150)
    Image = models.FileField('Изображение',upload_to='images/')
    Price = models.CharField('Цена', max_length=250)

    def __str__(self):
        return self.Product_Name

    class Meta:
        verbose_name = 'Лист продуктов'
        verbose_name_plural = 'Лист продуктов'

class Cartproducts(models.Model):
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    US = models.CharField('ID Пользователя', max_length=150)

    def __str__(self):
        return self.products

    def get_adsolute_url(self):
        return reverse('Cartproducts', kwargs={'products_id':self.pk})
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Товары в корзине'


class Category(models.Model):
    Name_Category = models.CharField('Название категории', max_length=150)

    def __str__(self):
        return self.Name_Category
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Buyer_Orders(models.Model):
    Products = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    User_id = models.CharField('ID Пользователя', max_length=150)
    Order_number = models.CharField('Номер заказ', max_length=150)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


# Create your models here.
