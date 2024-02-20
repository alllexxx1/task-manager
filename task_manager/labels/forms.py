from django import forms
from task_manager.labels.models import Label


class LabelCreateForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']
