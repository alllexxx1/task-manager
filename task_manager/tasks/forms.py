from django import forms
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']

    status = forms.ModelChoiceField(queryset=Status.objects.all())
    assignee = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
