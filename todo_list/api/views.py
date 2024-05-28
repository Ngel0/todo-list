from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from tasklist.models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskListApiView(ModelViewSet):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)


class TaskApiView(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.all()
    #http_method_names = ['get']
