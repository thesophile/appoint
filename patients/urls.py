from django.urls import path
from patients import views

urlpatterns = [
    path('', views.patients),
    path('success', views.success),
    
]