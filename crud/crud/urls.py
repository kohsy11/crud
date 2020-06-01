"""crud URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('detail/<int:key>', views.detail , name = 'detail' ),
    path('new/', views.new, name = 'new'),
    path('edit/<int:key>', views.edit, name = 'edit'),
    path('delete/<int:key>', views.delete, name = 'delete'),
    path('delete_comment/<int:key>/<int:comment_key>', views.delete_comment, name = 'delete_comment'),
    path('registration/signup', views.signup, name = 'signup'),
    path('registration/login', views.login, name = 'login'),
    path('registration/logout', views.logout, name = 'logout'),
    path('accounts/', include('allauth.urls')),
    path('mypage/<int:mykey>', views.mypage, name = 'mypage')
]
