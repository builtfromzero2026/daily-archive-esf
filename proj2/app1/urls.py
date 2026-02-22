from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('var1/', views.var1),
    path('var2/', views.var2),
    path('var3/',views.var3),
    path('var4/',views.var4),
    path('var5/',views.var5),
    
    
]
