from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm
from task_manager.custom_utils import AuthRequiredMixin


class UsersView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    ordering = ['id']


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User has been successfully registered')


class UpdateUserView(AuthRequiredMixin,
                     UserPassesTestMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User has been successfully changed')

    def test_func(self):
        user_pk = self.kwargs.get('pk')
        return self.request.user.pk == user_pk

    def handle_no_permission(self):
        msg_text = _("You haven't got permission to edit another user")
        messages.warning(self.request, msg_text)
        return redirect(reverse_lazy('users:users'))


class DeleteUserView(AuthRequiredMixin,
                     UserPassesTestMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User has been successfully deleted')

    def test_func(self):
        user_pk = self.kwargs.get('pk')
        return self.request.user.pk == user_pk

    def handle_no_permission(self):
        msg_text = _("You haven't got permission to edit another user")
        messages.warning(self.request, msg_text)
        return redirect(reverse_lazy('users:users'))
