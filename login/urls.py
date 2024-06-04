from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    #for login.html use the default accounts/login
]
