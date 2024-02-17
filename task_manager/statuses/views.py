from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreateForm
from task_manager.custom_utils import AuthRequiredMixin, DeletionProtectHandleMixin


class StatusesView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    ordering = ['pk']


class CreateStatusView(SuccessMessageMixin, AuthRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status has been successfully created')


class UpdateStatusView(SuccessMessageMixin, AuthRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status has been successfully updated')


class DeleteStatusView(SuccessMessageMixin,
                       AuthRequiredMixin,
                       DeletionProtectHandleMixin,
                       DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = redirect_url = reverse_lazy('statuses:statuses')
    success_message = _('Status has been successfully deleted')
    protection_msg = _("Status can't be deleted. It is linked to one or more tasks")
