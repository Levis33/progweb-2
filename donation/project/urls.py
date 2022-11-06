from django.urls import path
from project import views

# path('', painel, name='home'),

urlpatterns = [
    path('', views.home, name='home'),
]