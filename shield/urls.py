"""shield URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from shieldServer import views
from clockchain import clock
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('count/', views.order_count, name='orderCount'),
    path('addLending/', views.add_lending, name='addLending'),
    path("mine/", clock.mine),
    path("show/", clock.show),
    path('repayment/', views.repayment, name='repayment'),
    re_path(r'^index/(\w+).html$',views.others)
]
