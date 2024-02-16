from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    ListView, CreateView,
    DetailView
)
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskCreateForm
from task_manager.custom_utils import AuthRequiredMixin
from task_manager.users.models import User


class TasksView(AuthRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'


class DetailTaskView(DetailView):
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
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)
