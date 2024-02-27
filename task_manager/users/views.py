from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserCreateForm
from task_manager.mixins import (AuthRequiredMixin,
                                 UserPermissionMixin,
                                 DeletionProtectHandleMixin)


class UsersView(ListView):
    model = get_user_model()
    template_name = 'users/users.html'
    context_object_name = 'users'
    ordering = ['pk']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User has been successfully registered')


class UpdateUserView(AuthRequiredMixin,
                     UserPermissionMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User has been successfully changed')


class DeleteUserView(AuthRequiredMixin,
                     UserPermissionMixin,
                     DeletionProtectHandleMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_url = redirect_url = reverse_lazy('users:users')
    success_message = _('User has been successfully deleted')
    protection_msg = _("User can't be deleted. It is linked to one or more tasks")
