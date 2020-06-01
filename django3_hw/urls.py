"""django3_hw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app3 import views

urlpatterns = [
    path('registration/signup',views.signup, name="signup"),
    path('registration/login',views.login, name="login"),
    path('registration/logout',views.logout, name="logout"),
   
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:pk_clicked>',views.detail, name="detail"),
    path('edit/<int:pk_clicked>',views.edit, name="edit"),
    path('delete/<int:pk_clicked>',views.delete, name="delete"),
    path('delete_comment/<int:pk_clicked>/<int:comment_pk>',views.delete_comment,name="delete_comment"),
    path('mypage/',views.mypage,name="mypage"),
    path('accounts/',include('allauth.urls')),
]
