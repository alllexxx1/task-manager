from django import forms
from django_filters import (
    FilterSet, BooleanFilter,
    CharFilter,
    ModelChoiceFilter,
    # ModelMultipleChoiceFilter
)
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TasksFilter(FilterSet):

    class Meta:
        model = Task
        fields = ['name', 'status', 'executor', 'labels']

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

    executor = ModelChoiceFilter(
        label=_('Executor'),
        field_name='executor',
        queryset=get_user_model().objects.all()
    )

    labels = ModelChoiceFilter(
        label=_('Label'),
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
            return queryset.filter(executor=user)
        return queryset
