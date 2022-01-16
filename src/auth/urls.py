from django.urls import path, include
from .views import Register_Users

urlpatterns = [
    path('register/', Register_Users.as_view(), name='register-users'),
]