from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('password_update', views.password_update, name='password_update'),
    path('logout/', views.logout_user, name='logout_user'),
]
