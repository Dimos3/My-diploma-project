from django.urls import path
from . import views


urlpatterns = [
    path('post/<int:user_id>/', views.Create_an_order ,name='Create_an_order'),
    
]