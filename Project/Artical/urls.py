from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='Home'),
    path('bask', views.basket, name='baskK'),
    path('li', views.ListProducts, name='List'),
    path('About company', views.company, name='About company'),
    path('signup/', views.registration, name='signup'),
    path('post/g/<int:ID>/', views.Deleting_an_item ,name='Del'),
    path('post/<int:item_id>/', views.add_to_backet ,name='ADD'),
    path('GRM', views.Locl_GRM, name = 'GRM'),
    path('spark_plug', views.Locl_spark_plug, name = 'spark_plug'),
    path('Air_filter', views.Locl_Air_filter, name = 'Air_filter'),
    path('Fuel_tank', views.Locl_Fuel_tank, name='Fuel_tank'),
    path('Oil_filter', views.Locl_Oil_filter, name='Oil_filter'),
    path('spark', views.TEST ,name = 'spark'),
    path('Creating_orders', views.TEST , name = 'Creating orders'),
    path('Orders', views.display_of_Orders, name = 'Orders'),
    path('post/A/<int:Nomer>/', views.TeSt, name = 'Ord'),
    path('issue', views.issuelist, name = 'issue'),
    path('seaord', views.search, name = 'seaorders'), 
    path('post/B/<int:Nomer>/', views.orddelite, name = 'orddel')
]