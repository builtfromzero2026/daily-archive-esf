from django.urls import path
from . import views

urlpatterns = [
    path('support/', views.support),
    path('profile/', views.profile),
]
