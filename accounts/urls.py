from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('guest/', views.guest_register_view, name='guest_register'),
    #path('password_change/', views.change_password, name='change_password'),
]
