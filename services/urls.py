from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.providers_list, name='providers_list'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
