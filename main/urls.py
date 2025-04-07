from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('addpost/<username>/', views.add_post, name='addpost'),
    path('deletepost/<int:id>/', views.delete_post, name='deletepost'),
    path('fullpost/<int:id>/', views.full_post, name='fullpost'),
    path('<str:back>/<int:id>/readfullpost/',
         views.read_full_post, name='readfullpost'),
    path('editpost/<int:id>/', views.edit_post, name='editpost'),
    path('user/<username>/', views.show_user, name='user'),
    path('profile/', views.profile_page, name='profile'),
    path('password', views.change_password, name='changepassword')
]
