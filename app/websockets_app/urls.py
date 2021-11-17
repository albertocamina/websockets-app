"""websockets_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from websockets_app.views import HomeView


urlpatterns = [

    # URLs para la home
    path("",  login_required( HomeView.as_view() ), name="home" ),

    # URLs para login
    path("accounts/login/", auth_views.LoginView.as_view(), name="login" ),
    path("accounts/login/", auth_views.LogoutView.as_view(), name="logout" ),   

    # URLs del gestor de Topics
    path( "", include("gestor_topics.urls") ),

    # URL del gestor de dispositivos
    path( "", include("dispositivos.urls") )

]
