
from django.urls import path
from .views import RentInHome,RentInRegisterVIew,TenantLoginView,register_view, tenant_login_view
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', view=RentInHome.as_view(), name='home'),
    path('register/', view=RentInRegisterVIew.as_view(), name='register' ),
    # Custom login view
    path('login/', TenantLoginView.as_view(template_name='registration/login.html'), name='login'),

    # Custom logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]