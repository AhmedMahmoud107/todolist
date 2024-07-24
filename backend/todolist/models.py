from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class TodoListt(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title

class TodoTask(models.Model):
    title = models.CharField(max_length=100)
    content  = models.TextField()
    list = models.ForeignKey(TodoListt, on_delete=models.CASCADE ,related_name="tasks")

    def __str__(self) :
        return self.title