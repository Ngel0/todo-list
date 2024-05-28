from rest_framework.serializers import ModelSerializer

from tasklist.models import TaskList, Task


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'user', 'todo_list']
