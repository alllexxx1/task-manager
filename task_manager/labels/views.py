from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import AuthRequiredMixin, DeletionProtectHandleMixin
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
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label has been successfully created')


class UpdateLabelView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label has been successfully changed')


class DeleteLabelView(SuccessMessageMixin,
                      AuthRequiredMixin,
                      DeletionProtectHandleMixin,
                      DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = redirect_url = reverse_lazy('labels:labels')
    success_message = _('Label has been successfully deleted')
    protection_msg = _("Label can't be deleted. It is linked to one or more tasks")
