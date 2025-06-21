from django.views.static import serve
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list, product_detail

urlpatterns = [
     path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('', include('allauth.urls')),
    path('products/', views.product_list, name='product_list'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
