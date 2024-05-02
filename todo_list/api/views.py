from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasklist.models import Task
from .serializers import TaskSerializer


class TaskApiView(ModelViewSet):
    queryset = Task.objects.all()#добавить фильтр по юзеру
    serializer_class = TaskSerializer
    #http_method_names = ['get']
