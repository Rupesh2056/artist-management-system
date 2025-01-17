
from django.urls import path

from user.export import ArtistExportView
from user.views import ArtistListView, ArtistUserCreateView, UserCreateView, UserDeleteView, UserListView,UserUpdateView
from user.auth_views import  UserLoginView, UserLogoutView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="user_register"),
    path('login/', UserLoginView.as_view(),name="user_login"),
    path('logout/', UserLogoutView.as_view(),name="user_logout"),

    path("user/",UserListView.as_view(),name="user_list"),
    path("user/create/",UserCreateView.as_view(),name="user_create"),
    path("user/<int:pk>/update/",UserUpdateView.as_view(),name="user_update"),
    path("user/delete/",UserDeleteView.as_view(),name="user_delete"),


    path("artist/",ArtistListView.as_view(),name="artist_list"),
    path("artist/create/",ArtistUserCreateView.as_view(),name="artist_create"),
    path("artist/<int:pk>/update/",UserUpdateView.as_view(),name="artist_update"),
    path("artist/delete/",UserDeleteView.as_view(),name="artist_delete"),

    path("artist/export/",ArtistExportView.as_view(),name="artist_export"),




  
]
