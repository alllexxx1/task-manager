from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from task_manager.forms import LoginUserForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUserView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    success_url = 'index'
    success_message = _("You've successfully logged in")


class LogoutUserView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.info(request, _("You've successfully logged out"))
        return response
