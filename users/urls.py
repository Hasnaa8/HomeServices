from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import login, logout

app_name = "users"

urlpatterns = [
    path('favourite/', views.favourite_list, name='favourite'),
    path('favourite/add_to_favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
