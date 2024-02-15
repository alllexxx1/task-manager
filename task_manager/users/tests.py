from django.test import TestCase
from django.urls import reverse
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm
from task_manager.custom_utils import load_fixture


class UserRegistrationTestCase(TestCase):

    def setUp(self):
        self.users = load_fixture('test_users.json')
        self.registration_url = reverse('users:create')

    def test_register_valid_user(self):
        user_count_before = User.objects.count()
        response = self.client.post(self.registration_url,
                                    self.users['valid_user'])
        user_count_after = User.objects.count()
        new_user = User.objects.last()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertIsNotNone(new_user)
        self.assertEqual(user_count_after, user_count_before + 1)

    def test_register_invalid_user(self):
        response = self.client.post(self.registration_url,
                                    self.users['invalid_user'])
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'password2',
                             "The two password fields didn’t match.")

    def test_register_invalid_password(self):
        response = self.client.post(self.registration_url,
                                    self.users['short_password_user'])

        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'password2',
                             'This password is too short. '
                             'It must contain at least 3 characters.')

    def test_register_form(self):
        user = self.users['valid_user']
        form = UserCreateForm(user)
        self.assertTrue(form.is_valid())


class UserUpdateTestCase(TestCase):
    def setUp(self):
        self.users = load_fixture('test_users.json')

    def test_update_user(self):
        user = User.objects.create_user(**self.users['registered_user'])
        update_url = reverse('users:update', args=[user.pk])
        self.client.login(username='rodal', password='a23455555')
        response = self.client.post(update_url, self.users['updated_user'])
        updated_user = User.objects.get(pk=user.pk)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertEqual(updated_user.first_name, 'Jerome')
        self.assertEqual(updated_user.username, 'sailman')


class UserDeleteTestCase(TestCase):
    def setUp(self):
        self.users = load_fixture('test_users.json')

    def test_delete_user(self):
        user = User.objects.create_user(**self.users['registered_user'])
        deletion_url = reverse('users:delete', args=[user.pk])
        self.client.login(username='rodal', password='a23455555')
        response = self.client.post(deletion_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertFalse(User.objects.last())


class UsersViewTestCase(TestCase):
    fixtures = ['user.json', 'auth.json']

    def test_get_users(self):
        response = self.client.get(reverse('users:users'))
        users = response.context['users']
        user1 = User.objects.get(username='Pterry')
        user2 = User.objects.get(username='Nellie')
        user3 = User.objects.get(username='huda')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertEqual(users.count(), 3)
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user3, users)


class UserLoginTestCase(TestCase):

    def setUp(self):
        self.users = load_fixture('test_users.json')
        self.login_url = reverse('login')

    def test_user_login_success(self):
        User.objects.create_user(**self.users['login_user'])
        response = self.client.post(self.login_url,
                                    {'username': 'rodal', 'password': 'a23455555'},
                                    follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index'))

        user = response.context['user']
        self.assertTrue(user.is_authenticated)

    def test_user_login_failure(self):
        User.objects.create_user(**self.users['login_user'])
        response = self.client.post(self.login_url,
                                    {'username': 'Ronald', 'password': 'wrong_password'},
                                    follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password')

        user = response.context['user']
        self.assertFalse(user.is_authenticated)
