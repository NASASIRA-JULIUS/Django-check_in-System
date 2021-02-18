from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('users/',views.users, name="users" ),
    path('register/',views.register, name="register" ),
    path('update/<str:pk>/',views.update_user, name="update" ),
    path('delete/<str:pk>/',views.delete_user, name="delete" ),

    path('registerPage/',views.registerPage, name="registerPage" ),
    path('login/',views.loginPage, name="login" ),
    path('logout/', views.logoutUser, name="logout"),

    path('user/', views.userPage, name="user-page"),
]