
from django.urls import path

from user.views import UserLoginView, UserLogoutView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="user_register"),
    path('login/', UserLoginView.as_view(),name="user_login"),
    path('logout/', UserLogoutView.as_view(),name="user_logout"),
  
]
