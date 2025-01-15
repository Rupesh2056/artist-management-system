
from django.urls import path

from user.views import UserCreateView, UserDeleteView, UserListView, UserLoginView, UserLogoutView, UserRegistrationView, UserUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="user_register"),
    path('login/', UserLoginView.as_view(),name="user_login"),
    path('logout/', UserLogoutView.as_view(),name="user_logout"),

    path("user/",UserListView.as_view(),name="user_list"),
    path("user/create/",UserCreateView.as_view(),name="user_create"),
    path("user/<int:pk>/update/",UserUpdateView.as_view(),name="user_update"),
    path("user/delete/",UserDeleteView.as_view(),name="user_delete"),
  
]
