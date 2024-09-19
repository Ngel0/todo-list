import pytest
from django.contrib.auth.models import User
from tests.factories import UserFactory, TaskListFactory, TaskFactory
from tasklist.models import TaskList, Task


@pytest.mark.django_db
def test_create_user():
    user = UserFactory()  # Same as UserFactory.create()
    assert user.pk is not None


@pytest.mark.django_db
def test_create_task_list():
    task_list = TaskListFactory()
    assert task_list.pk is not None


@pytest.mark.django_db
def test_create_task():
    task = TaskFactory()
    assert task.pk is not None


@pytest.mark.django_db
def test_delete_user():
    user = UserFactory()
    user.delete()
    with pytest.raises(User.DoesNotExist):
        User.objects.get(pk=user.pk)


@pytest.mark.django_db
def test_delete_task_list():
    task_list = TaskListFactory()
    task_list.delete()
    with pytest.raises(TaskList.DoesNotExist):
        TaskList.objects.get(pk=task_list.pk)


@pytest.mark.django_db
def test_delete_task():
    task = TaskFactory()
    task.delete()
    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(pk=task.pk)
