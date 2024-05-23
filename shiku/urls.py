from django.urls import path
from .import views

urlpatterns = [
    path('hey/', views.say_shiku)
]