from django.urls import path
from . import views

urlpatterns = [
    path("",views.Login,name='login'),
    path("home/",views.Home,name='home'),
    path("profile/",views.Profile,name='profile'),
    path("logout/",views.Logout,name='logout'),
    path("register/",views.Register,name='register'),   
    path("update/",views.Update_profile,name='update'),
]
