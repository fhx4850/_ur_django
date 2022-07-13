from django.urls import path
from . import views


urlpatterns = [
    path('profile/<slug:slug>/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/<slug:slug>/edit/', views.ProfileEdit.as_view(), name='edit_profile')
]