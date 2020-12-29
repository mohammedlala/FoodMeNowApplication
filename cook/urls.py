from django.urls import path
from . import views

urlpatterns = [
    path('cook-login', views.cookLogin, name='cook-login'),
    path('cook-register', views.cookRegister, name='cook-register'),
    path('cook-home', views.cookHome, name='cook-home'),
    path('cook-logout', views.cookLogout, name='cook-logout'),
    path('reqLoad', views.reqLoad, name='reqLoad'),
    path('req-details/<int:id>', views.reqDetails, name='req-details'),
]
