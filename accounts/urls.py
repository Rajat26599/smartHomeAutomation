from django.urls import path, include
# from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
