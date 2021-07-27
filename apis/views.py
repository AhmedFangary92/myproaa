from rest_framework import generics
from todolist import models
from .serializers import TodoListSerializer

class TodoListApi(generics.ListCreateAPIView):
    queryset = models.List.objects.all()
    serializer_class = TodoListSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.List.objects.all()
    serializer_class = TodoListSerializer