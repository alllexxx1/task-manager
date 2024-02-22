from django import forms
from django.utils.translation import gettext as _
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee', 'labels']

    name = forms.CharField(
        label=_('Name'),
        max_length=150,
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea()
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label=_('Status'),
    )
    assignee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label=_('Assignee'),
        required=False
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Labels'),
        required=False
    )
