from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import TodoListt, TodoTask
from .serializers import TodolistSerializer, TodoTaskContntSerializer

class TodolistListCreateApiView(generics.ListCreateAPIView):
    queryset = TodoListt.objects.all()
    serializer_class = TodolistSerializer
    lookup_field = 'pk'

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


class TodoTaskListCreateApiView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskContntSerializer


class TodoTaskRetriveUpdateDelete(
        generics.RetrieveAPIView,
        generics.DestroyAPIView,
        generics.UpdateAPIView,
    ):
    # queryset = TodoTask.objects.all()
    serializer_class = TodoTaskContntSerializer

    def get_queryset(self):
        # Retrieve the `lsitpk` from the URL parameter
        lsitpk = self.kwargs['lsitpk']
        
        # Filter tasks based on the list_id (`lsitpk`)
        queryset = TodoTask.objects.filter(list_id=lsitpk)
        
        return queryset

    def get_object(self):
        # Retrieve the `taskpk` from the URL parameter
        taskpk = self.kwargs['taskpk']
        
        # Get the specific task based on taskpk within the filtered queryset
        queryset = self.get_queryset()
        task = get_object_or_404(queryset, pk=taskpk)
        
        return task