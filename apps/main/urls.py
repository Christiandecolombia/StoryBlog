from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
]