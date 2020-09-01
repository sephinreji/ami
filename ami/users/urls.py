from django.contrib import admin
from django.urls import path
from . import views
from .views import IndexView, LoginView, LogoutView, AboutView

urlpatterns = [

    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='loginview'),
    path('logout/',LogoutView.as_view(),name='logoutview'),
    path('about/',AboutView.as_view(),name='about')
]
