from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TaskList, Task


# TaskList views
class TaskListList(LoginRequiredMixin, ListView):
    model = TaskList
    context_object_name = 'tasklists'

    def get_queryset(self):
        return TaskList.objects.filter(user=self.request.user)


class TaskListDetail(LoginRequiredMixin, DetailView):
    model = TaskList
    context_object_name = 'tasklist'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(todo_list=self.object)
        return context


class TaskListCreate(LoginRequiredMixin, CreateView):
    model = TaskList
    fields = ['title']
    success_url = reverse_lazy('tasklists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskListUpdate(LoginRequiredMixin, UpdateView):
    model = TaskList
    fields = ['title']
    success_url = reverse_lazy('tasklists')


class TaskListDelete(LoginRequiredMixin, DeleteView):
    model = TaskList
    context_object_name = 'tasklist'
    success_url = reverse_lazy('tasklists')


# Task views
class TaskItemList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)#.order_by('todo_list', 'is_completed')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['incomplete_tasks_count'] = context['tasks'].filter(is_completed=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasklist/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['todo_list', 'title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['todo_list', 'title', 'description', 'is_completed']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
