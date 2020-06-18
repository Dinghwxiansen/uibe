"""uibe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
import django_cas_ng
import django_cas_ng.views as cas_views
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from apps.base import logout, login
from apps.base import urls as base_urls

urlpatterns = [
    # drf文档，title自定义
    path('docs', include_docs_urls(title='南北软件')),

    path('base/', include(base_urls)),
    path('warning/', include('apps.warning.urls')),
    path('portrait/', include('apps.portrait.urls')),
    #  cas单点登录
    # path('login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    # path('logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('login/', login.LoginView.as_view(), name="login"),
    path('logout/', logout.LogoutView.as_view(), name="logout"),

]
