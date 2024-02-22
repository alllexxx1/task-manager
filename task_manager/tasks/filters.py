from django import forms
from django_filters import (
    FilterSet, BooleanFilter,
    CharFilter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter
)
from django.utils.translation import gettext as _
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TasksFilter(FilterSet):

    class Meta:
        model = Task
        fields = ['name', 'status', 'assignee', 'labels']

    name = CharFilter(
        label=_('Task name'),
        field_name='name',
        lookup_expr='icontains'
    )

    status = ModelChoiceFilter(
        label=_('Status'),
        field_name='status',
        queryset=Status.objects.all()
    )

    assignee = ModelChoiceFilter(
        label=_('Assignee'),
        field_name='assignee',
        queryset=User.objects.all()
    )

    labels = ModelMultipleChoiceFilter(
        label=_('Labels'),
        field_name='labels',
        queryset=Label.objects.all()
    )

    assigned_tasks = BooleanFilter(
        label=_('Only tasks assigned to me'),
        widget=forms.CheckboxInput,
        method='get_assigned_tasks'
    )

    personal_tasks = BooleanFilter(
        label=_('Only tasks created by me'),
        widget=forms.CheckboxInput,
        method='get_personal_tasks'
    )

    def get_personal_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    def get_assigned_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(assignee=user)
        return queryset
