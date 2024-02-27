from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']

    name = forms.CharField(
        label=_('Name'),
        max_length=100
    )
