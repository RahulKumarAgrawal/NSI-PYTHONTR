from django.urls import path, include
from .views import (
    StoreListAPIView
)
from products import views
urlpatterns = [
    path('store-list/', StoreListAPIView.as_view(), name='store-list'),
]