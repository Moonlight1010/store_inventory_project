from .views import register, login_view, logout_view
from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('', login_view, name='login-page'),
    path('register/', register, name='register-page'),
    path('logout/', logout_view, name='logout-view'),
    path('password_reset/', PasswordResetView.as_view(template_name='user_registration/password_reset.html'), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='user_registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='user_registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='user_registration/password_reset_done.html'), name='password_reset_done'),
]