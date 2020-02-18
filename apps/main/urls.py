from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('frontpage/', views.frontpage, name='frontpage'),
    path('storypage/', views.storypage, name='storypage'),
    path('addstory/', views.addstory, name='addstory'),
    # path('postRegister', views.postRegister, name='postRegister'),
    # path('postLogin', views.postLogin, name='postLogin'),
    path("logout", views.logout, name="logout"),
    ] 