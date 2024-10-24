from django.urls import path
from . import views

urlpatterns = [
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logout'),
    path('register',views.registerpage,name='register'),
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('profile/<str:pk>/',views.UserProfile,name='user-profile'),
    path('create-room/',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>/',views.UpdateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.DeleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.DeleteMessage,name='delete-message'),
    path('update-user/',views.UpdateUser,name='update-user'),
    path('topics/',views.topicspage,name='topics'),
    path('activity/',views.activitypage,name='activity'),
]
