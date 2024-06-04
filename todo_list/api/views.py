from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from tasklist.models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskListApiView(ModelViewSet):
    """
    ViewSet for TaskList model.
    Handles CRUD operations for TaskLists.
    """
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)


class TaskListTasksApiView(ListAPIView):
    """
    APIView for listing tasks of a specific tasklist.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, todo_list=self.kwargs['pk'])


class TaskApiView(ModelViewSet):
    """
    ViewSet for Task model.
    Handles CRUD operations for Tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
