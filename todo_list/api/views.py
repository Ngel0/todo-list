from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from tasklist.models import Task
from .serializers import TaskSerializer


class TaskApiView(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    #http_method_names = ['get']
