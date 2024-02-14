from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, View, DeleteView
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


class UpdateUserView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User has been successfully changed')


class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users')
    success_message = _('User has been successfully deleted')


# class DeleteUserView(View):
#     def get(self, request, *args, **kwargs):
#         user_pk = kwargs.get('pk')
#         user = User.objects.get(pk=user_pk)
#         return render(
#             request,
#             'users/delete.html',
#             {'user': user}
#         )
#
#     def post(self, request, *args, **kwargs):
#         user_pk = kwargs.get('pk')
#         user = User.objects.get(pk=user_pk)
#         if user:
#             user.delete()
#             messages.success(request, _('User has been successfully deleted'))
#         return redirect('users:users')
