from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-register', views.userRegister, name='user-register'),
    path('user-login', auth_views.LoginView.as_view(template_name='user_login.html'),
         name='user-login'),
    path('user-home', views.userHome, name='user-home'),
    path('user-logout', views.userLogout, name='user-logout'),
    path('area-load', views.areaLoad, name='area-load'),
    path('search-cook', views.searchCook, name='search-cook'),
    path('result-detail/<str:email>/', views.resultDetail, name='result-detail'),
    path('req-create', views.reqCreate, name='req-create'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
]
