from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']

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
    executor = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        label=_('Executor'),
        required=False
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label=_('Labels'),
        required=False
    )
