from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class AuthRequiredMixin(LoginRequiredMixin):
    msg_text = _('Access denied. Please log in.')
    redirect_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, self.msg_text)
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
