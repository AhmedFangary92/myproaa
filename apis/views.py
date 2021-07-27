from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todolist.models import List
from .serializers import TodoListSerializer

class TodoListApi(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = TodoListSerializer


class ItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = TodoListSerializer