from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
import json
import os


class AuthRequiredMixin(LoginRequiredMixin):
    msg_text = _('Access denied. Please log in.')
    redirect_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, self.msg_text)
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)


def load_fixture(path):
    with open(os.path.abspath(f'task_manager/fixtures/{path}'), 'r') as file:
        return json.loads(file.read())
