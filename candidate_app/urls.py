from django.contrib import admin
from django.urls import path
from .views import ChangePasswordView
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', MyLoginView.as_view(), name='user-login'),
    path('index/', index, name='index'),
    path('create_profile/', create_profile, name='create_profile'),
    path('update/<int:pk>', CandidateUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CandidateDeleteView.as_view(), name='delete'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('search/', query, name='search'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles', CandidateProfileListView.as_view(), name='profiles'),
    path('profiles/<int:pk>', CandidateProfileDetailView.as_view(), name='profile-detail'),
]