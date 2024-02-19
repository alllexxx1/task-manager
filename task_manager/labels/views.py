from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.custom_utils import AuthRequiredMixin, DeletionProtectHandleMixin


class LabelsView(ListView):
    pass


class CreateLabelView(CreateView):
    pass


class UpdateLabelView(UpdateView):
    pass


class DeleteLabelView(DeleteView):
    pass
