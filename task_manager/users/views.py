from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, View
from django.utils.translation import gettext as _
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm


class UsersView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User has been successfully registered')


class UpdateUserView(View):

    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        form = UserCreateForm(instance=user)
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_pk': user_pk}
        )

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('User has been successfully changed'))
            return redirect('users:users')
        return render(
            request,
            'users/update.html',
            {'form': form, 'user_pk': user_pk}
        )


class DeleteUserView(View):
    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        return render(
            request,
            'users/delete.html',
            {'user': user}
        )

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        if user:
            user.delete()
            messages.success(request, _('User has been successfully deleted'))
        return redirect('users:users')
