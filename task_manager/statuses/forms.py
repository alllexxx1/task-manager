from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status


class StatusCreateForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ['name']

    name = forms.CharField(
        label=_('Name'),
        max_length=100
    )
