import factory

from django.contrib.auth.models import User
from tasklist.models import TaskList, Task


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user_%d' % n)
    email = factory.Sequence(lambda n: 'user_%d@example.com' % n)
    # username = factory.Sequence('user{0}'.format)
    # email = factory.Sequence('user{0}@example.com'.format)
    password = factory.PostGenerationMethodCall('set_password', 'password')


class TaskListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskList

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'tasklist_%d' % n)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'task_%d' % n)
    todo_list = factory.SubFactory(TaskListFactory)
    # other fields here?
