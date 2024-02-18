from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
import json
import os


class AuthRequiredMixin(LoginRequiredMixin):
    not_auth_msg = _('Access denied. Please log in.')
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, self.not_auth_msg)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    no_permission_msg = _("You haven't got permission to edit another user")
    users_url = reverse_lazy('users:users')

    def test_func(self):
        user_pk = self.kwargs.get('pk')
        return self.request.user.pk == user_pk

    def handle_no_permission(self):
        messages.warning(self.request, self.no_permission_msg)
        return redirect(self.users_url)


class DeletionProtectHandleMixin:
    protection_msg = None
    redirect_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request, self.protection_msg)
            return redirect(self.redirect_url)


class AuthorPermissionMixin(UserPassesTestMixin):
    no_author_permission_msg = _('Task can be deleted only by its author')
    tasks_url = reverse_lazy('tasks:tasks')

    def test_func(self):
        task = self.get_object()
        return self.request.user.username == task.author.username

    def handle_no_permission(self):
        messages.warning(self.request, self.no_author_permission_msg)
        return redirect(self.tasks_url)


def load_fixture(path):
    with open(os.path.abspath(f'task_manager/fixtures/{path}'), 'r') as file:
        return json.loads(file.read())
