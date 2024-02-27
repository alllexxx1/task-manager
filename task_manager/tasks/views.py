from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, DetailView,
    UpdateView, DeleteView
)
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskCreateForm
from task_manager.mixins import (
    AuthRequiredMixin,
    AuthorPermissionMixin
)
from django_filters.views import FilterView
from task_manager.tasks.filters import TasksFilter
from django.contrib.auth import get_user_model


class TasksView(AuthRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    ordering = ['pk']
    filterset_class = TasksFilter


class DetailTaskView(AuthRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class CreateTaskView(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task has been successfully created')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = get_user_model().objects.get(pk=user.pk)
        return super().form_valid(form)


class UpdateTaskView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task has been successfully changed')


class DeleteTaskView(AuthRequiredMixin,
                     AuthorPermissionMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task has been successfully deleted')
