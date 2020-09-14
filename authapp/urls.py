from django.urls import path, include
from .views import (
    UserListView,
    UserDetailView
)
from authapp import views
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('user-detail/<str:pk>/', UserDetailView.as_view(), name="user-detail"),
    
]