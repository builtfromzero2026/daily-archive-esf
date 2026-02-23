from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    # path('<slug:x>',views.product_details_view, name="product-details"),
    
]
