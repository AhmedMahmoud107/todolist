from django.shortcuts import render

from rest_framework import generics

from .models import TodoListt, TodoTask
from .serializers import TodolistSerializer, TodoTaskSerializer, TodoTaskContntSerializer

class TodolistListCreateApiView(generics.ListCreateAPIView):
    queryset = TodoListt.objects.all()
    serializer_class = TodolistSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return TodoListt.objects.none()
        return qs.filter(user=request.user)
        


class TodolistRetriveUpdateDelete(
        generics.RetrieveAPIView,
        generics.DestroyAPIView,
        generics.UpdateAPIView,
    ):
    queryset = TodoListt.objects.all()
    serializer_class = TodolistSerializer
    lookup_field = 'pk'

class TodoTaskListCreateApiView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskContntSerializer



class TodoTaskRetriveUpdateDelete(
        generics.RetrieveAPIView,
        generics.DestroyAPIView,
        generics.UpdateAPIView,
    ):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskContntSerializer
    lookup_field = 'pk'
