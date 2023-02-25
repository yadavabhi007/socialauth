from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignUp.as_view(), name='signup'),
    path('login/',views.UserLogin.as_view(), name='login'),
    path('logout/',views.UserLogout.as_view(), name='logout'),
    path('profile/',views.MyProfile.as_view(), name='profile'),
    path('changepass/',views.ChangePass.as_view(), name='changepass'),
   
]