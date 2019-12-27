from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
]