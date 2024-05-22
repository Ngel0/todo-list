from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(TaskList, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['is_completed']
