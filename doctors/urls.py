from django.urls import path
from doctors import views

urlpatterns = [
    path('', views.doctors),
    
]