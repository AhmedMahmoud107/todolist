from rest_framework import serializers

from .models import TodoTask, TodoListt

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = [
            'title',
        ]


class TodoTaskContntSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = [
            'title',
            'content',
            'list',
        ]


class TodolistSerializer(serializers.ModelSerializer):
    tasks = TodoTaskSerializer(many=True, read_only=True)
    # content = TodoTaskContntSerializer(many=True, read_only=True)
    class Meta:
        model = TodoListt
        fields = [
            'title',   
            'tasks',
            # 'content',
        ]
