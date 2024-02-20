from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from task_manager.custom_utils import AuthRequiredMixin, DeletionProtectHandleMixin
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelCreateForm


class LabelsView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    ordering = ['pk']


class CreateLabelView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/create.html'
    success_message = _('Label has been successfully created')
    success_url = reverse_lazy('labels:labels')


class UpdateLabelView(UpdateView):
    pass


class DeleteLabelView(DeleteView):
    pass
