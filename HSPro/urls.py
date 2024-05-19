"""
URL configuration for HSPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users import views as user_views
from bookings import views as booking_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('edit-profile/', user_views.edit_profile, name='edit_profile'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<int:pk>/', user_views.profile, name='profile_pk'),

    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
    #      name='password_reset'),
    # path('password-reset-done/',
    #      auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
    #      name='password_reset_done'),
    # path('password-reset-confirm/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
    #      name='password_reset_complete'),
    path('settings/', user_views.settings, name='settings'),
    path('password-change/', user_views.change_password, name='password_change'),
    path('password-change-done/', user_views.password_change_done, name='password_change_done'),
    path('email-change/', user_views.change_email, name='email_change'),
    path('delete-account/', user_views.delete_account, name='delete_account'),
    path('edit-work-info/', user_views.edit_work_info, name='edit_work_info'),
    path('booking_user/<int:pk>', booking_views.booking_user, name='booking_user' ),
    path('booking_user/<int:pk>', booking_views.booking_user, name='booking_user' ),
    path('delete_order/<int:pk>' ,booking_views.delete_order, name='delete_order'),
    path('edit_booking/<int:pk>' ,booking_views.edit_booking, name='edit_booking'),
    path('delete_appointment/<int:pk>' ,booking_views.delete_appointment, name='delete_appointment'),
    path('complete_appointment/<int:pk>' ,booking_views.complete_appointment, name='complete_appointment'),
    path('confirm_appointment/<int:pk>' ,booking_views.confirm_appointment, name='confirm_appointment'),
    path('my_orders/' ,booking_views.my_orders, name='my_orders'),
    path('my_orders/pending/' ,booking_views.my_orders_pending, name='my_orders_pending'),
    path('my_orders/confirmed/' ,booking_views.my_orders_confirmed, name='my_orders_confirmed'),
    path('my_orders/completed' ,booking_views.my_orders_completed, name='my_orders_completed'),
    path('my_schedule/' ,booking_views.my_schedule, name='my_schedule'),
    path('my_schedule/pending/' ,booking_views.my_schedule_pending, name='my_schedule_pending'),
    path('my_schedule/confirmed/' ,booking_views.my_schedule_confirmed, name='my_schedule_confirmed'),
    path('my_schedule/completed/' ,booking_views.my_schedule_completed, name='my_schedule_completed'),
    path('appointment_details_prov/<int:pk>/' ,booking_views.appointment_details_prov, name='appointment_details_prov'),
    path('appointment_details_cust/<int:pk>/' ,booking_views.appointment_details_cust, name='appointment_details_cust'),
    
    path('users', include('users.urls')),
    path('', include('services.urls')),
    path('api-auth/', include('rest_framework.urls'))

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
