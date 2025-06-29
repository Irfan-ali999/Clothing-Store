"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# myproject/urls.py
# from django.contrib import admin
# from django.urls import path
# from myapp.views import home

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),
# ]

from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
#     path('grappelli/', include('grappelli.urls')),  # Grappelli URL
    
# ] 


from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', include('allauth.urls')),
     path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('products/', views.product_list, name='product_list'),
]