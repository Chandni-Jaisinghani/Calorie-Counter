"""ccproject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from ccapp.views import home,ufoodlist,uhealthyrecipes,ulogin,usignup,ulogout,ufoodlog,uaddfooditem,up,ucustomized,uviewdetails,uhacks
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")), #most important
    path('',include("ccapp.urls")), #my app urls
    path("",home,name="home"),
    path("ufoodlist/",ufoodlist,name="ufoodlist"),
    path("uhealthyrecipes/",uhealthyrecipes,name="uhealthyrecipes"),
    path("ulogin/",ulogin,name="ulogin"),
    path("usignup/",usignup,name="usignup"),
    path("ulogout/",ulogout,name="ulogout"),
    path("ufoodlog/",ufoodlog,name="ufoodlog"),
    path("uaddfooditem/",uaddfooditem,name="uaddfooditem"),
    path("up/",up,name="up"),
    path("ucustomized/",ucustomized,name="ucustomized"),
    path("uviewdetails/",uviewdetails,name="uviewdetails"),
    path("uhacks/",uhacks,name="uhacks"),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
