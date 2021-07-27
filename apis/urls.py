from django.urls import path
from .views import TodoListApi, ItemDetail


urlpatterns = [
    path('', TodoListApi.as_view()),
    path('<int:pk>/', ItemDetail.as_view()),
]