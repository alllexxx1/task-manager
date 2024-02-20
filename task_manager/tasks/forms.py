from django import forms
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee', 'labels']

    status = forms.ModelChoiceField(queryset=Status.objects.all())
    assignee = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    labels = forms.ModelMultipleChoiceField(queryset=Label.objects.all(), required=False)
