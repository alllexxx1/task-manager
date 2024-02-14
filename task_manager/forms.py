from task_manager.users.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
