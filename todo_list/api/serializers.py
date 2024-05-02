from rest_framework.serializers import ModelSerializer

from tasklist.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
