from django.shortcuts import render
from authapp.models import *
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from .serializers import *
from .models import *


class StoreListAPIView(generics.ListAPIView):
	authentication_classes = [SessionAuthentication]
	model = Store
	queryset = Store.objects.all()
	serializer_class = StoreListSerializer

	def get_queryset(self, *args, **kwargs):
		return Store.objects.filter(user=self.request.user)