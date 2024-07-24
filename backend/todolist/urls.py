from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodolistListCreateApiView.as_view(), name='todolist'),
    path('<int:pk>/', views.TodolistRetriveUpdateDelete.as_view(), name='todolist-update'),
    path('<int:pk>/create/', views.TodoTaskListCreateApiView.as_view(), name='task-create'),
    path('<int:pk>/<int:id>/', views.TodoTaskRetriveUpdateDelete.as_view(), name='task-update'),
]