from django.test import TestCase
from django.urls import reverse

from task_manager.custom_utils import load_fixture
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskCRUDTestCase(TestCase):
    fixtures = ['user.json', 'auth.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.tasks = load_fixture('test_tasks.json')

    def test_create_task(self):
        post_url = reverse('tasks:create')
        response = self.client.post(post_url, self.tasks['valid_task'])

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks:tasks'))
        self.assertEqual(Task.objects.all().count(), 3)

    def test_read_tasks(self):
        get_url = reverse('tasks:tasks')
        response = self.client.get(get_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
