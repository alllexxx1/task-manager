from django import forms
from django_filters import FilterSet, BooleanFilter, CharFilter
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _


class TasksFilter(FilterSet):

    name = CharFilter(
        label=_('Task name'),
        field_name='name',
        lookup_expr='icontains'
    )

    assigned_task = BooleanFilter(
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

    class Meta:
        model = Task
        fields = ['name', 'status', 'assignee']
