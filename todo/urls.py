# todo/urls.py

from django.urls import path
from .views import (
    TodosAPIView,
    TodoAPIView,
    DoneTodosAPIView,
    DoneTodoAPIView,
    TodoListCreateAPIView,
    TodoRetrieveUpdateDestroyAPIView,
    DoneTodoListAPIView
)

urlpatterns = [
    path('todo/', TodosAPIView.as_view(), name='todos'),
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-retrieve-update-delete'),
    path('todos/done/', DoneTodoListAPIView.as_view(), name='done-todo-list')
]
