from rest_framework import generics
from .models import TestUser
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = TestUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestUser.objects.all()
    serializer_class = UserSerializer