
from django.urls import path

from user.views import UserListView, UserLoginView, UserLogoutView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="user_register"),
    path('login/', UserLoginView.as_view(),name="user_login"),
    path('logout/', UserLogoutView.as_view(),name="user_logout"),

    path("user/",UserListView.as_view(),name="user_list")
  
]
