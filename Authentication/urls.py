from django.urls import path
from . import views


urlpatterns = [
    path('accounts/login/', views.login_view),
    path('accounts/logout/', views.logout_view),
    path('accounts/register/', views.register_view),
]