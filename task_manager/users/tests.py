from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.users.forms import UserCreateForm
import json
import os


class UserRegistrationTestCase(TestCase):

    def setUp(self):
        self.users = load_fixture('users_to_create.json')
        self.registration_url = reverse('users:create')

    def test_register_valid_user(self):
        user_count_before = get_user_model().objects.count()
        response = self.client.post(self.registration_url,
                                    self.users['valid_user'])
        user_count_after = get_user_model().objects.count()
        new_user = get_user_model().objects.last()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertIsNotNone(new_user)
        self.assertEqual(user_count_after, user_count_before + 1)

    def test_register_invalid_user(self):
        response = self.client.post(self.registration_url,
                                    self.users['invalid_user'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.all().count(), 0)

    def test_register_invalid_password(self):
        response = self.client.post(self.registration_url,
                                    self.users['short_password_user'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.all().count(), 0)

    def test_register_form(self):
        user = self.users['valid_user']
        form = UserCreateForm(user)
        self.assertTrue(form.is_valid())


class UserUpdateTestCase(TestCase):
    def setUp(self):
        self.users = load_fixture('users_to_create.json')

    def test_update_user(self):
        user = get_user_model().objects.create_user(**self.users['registered_user'])
        update_url = reverse('users:update', args=[user.pk])
        self.client.login(username='rodal', password='a23455555')
        response = self.client.post(update_url, self.users['updated_user'])
        updated_user = get_user_model().objects.get(pk=user.pk)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertEqual(updated_user.first_name, 'Jerome')
        self.assertEqual(updated_user.username, 'sailman')


class UserDeleteTestCase(TestCase):
    def setUp(self):
        self.users = load_fixture('users_to_create.json')

    def test_delete_user(self):
        user = get_user_model().objects.create_user(**self.users['registered_user'])
        deletion_url = reverse('users:delete', args=[user.pk])
        self.client.login(username='rodal', password='a23455555')
        response = self.client.post(deletion_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertFalse(get_user_model().objects.last())


class UsersReadTestCase(TestCase):
    fixtures = ['users.json']

    def test_read_users(self):
        response = self.client.get(reverse('users:users'))
        users = response.context['users']
        user1 = get_user_model().objects.get(username='Pterry')
        user2 = get_user_model().objects.get(username='Nellie')
        user3 = get_user_model().objects.get(username='huda')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertEqual(users.count(), 3)
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)


class UserLoginTestCase(TestCase):

    def setUp(self):
        self.users = load_fixture('users_to_create.json')
        self.login_url = reverse('login')

    def test_user_login_success(self):
        get_user_model().objects.create_user(**self.users['login_user'])
        response = self.client.post(self.login_url,
                                    {'username': 'rodal', 'password': 'a23455555'},
                                    follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))

        user = response.context['user']
        self.assertTrue(user.is_authenticated)

    def test_user_login_failure(self):
        get_user_model().objects.create_user(**self.users['login_user'])
        response = self.client.post(self.login_url,
                                    {'username': 'Ronald', 'password': 'wrong_password'},
                                    follow=True)

        self.assertEqual(response.status_code, 200)

        user = response.context['user']
        self.assertFalse(user.is_authenticated)


def load_fixture(path):
    with open(os.path.abspath(f'task_manager/fixtures/{path}'), 'r') as file:
        return json.loads(file.read())
