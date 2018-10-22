from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('password_update', views.password_update, name='password_update'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                email_template_name='password_reset_email.html',
                                                                subject_template_name='password_reset_subject.txt',
                                                                success_url='password_reset/done/'),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url='password_reset/complete/'),
         name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('logout/', views.logout_user, name='logout_user'),
]
