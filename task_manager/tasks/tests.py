from django.test import TestCase
from django.urls import reverse
from task_manager.custom_utils import load_fixture
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskCRUDTestCase(TestCase):
    fixtures = ['users.json', 'auth.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.tasks = load_fixture('tasks_to_create.json')

    def test_create_valid_task(self):
        post_url = reverse('tasks:create')
        response = self.client.post(post_url, self.tasks['valid_task'])

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks:tasks'))
        self.assertEqual(Task.objects.all().count(), 3)

    def test_create_invalid_task(self):
        post_url = reverse('tasks:create')
        response = self.client.post(post_url, self.tasks['invalid_task'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 2)
        self.assertFormError(response.context['form'], 'status',
                             'This field is required.')

    def test_read_tasks(self):
        get_url = reverse('tasks:tasks')
        response = self.client.get(get_url)
        tasks = response.context['tasks']
        task = Task.objects.get(pk=1)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertIn(task, tasks)

    def test_read_task(self):
        task = Task.objects.get(pk=2)
        get_url = reverse('tasks:task', args=[task.pk])
        response = self.client.get(get_url)
        response_text = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task.html')
        self.assertIn(task.name, response_text)
        self.assertIn(task.description, response_text)
        self.assertIn('Philip Pullman', response_text)

    def test_update_task(self):
        task = Task.objects.get(pk=1)
        post_url = reverse('tasks:update', args=[task.pk])
        response = self.client.post(post_url, self.tasks['valid_task'])

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks:tasks'))
        task.refresh_from_db()
        self.assertEqual(task.name, 'New task #1')

    def test_delete_task(self):
        task = Task.objects.get(pk=2)
        post_url = reverse('tasks:delete', args=[task.pk])
        response = self.client.post(post_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks:tasks'))
        self.assertEqual(Task.objects.all().count(), 1)


class FilterFormTestCase(TestCase):
    fixtures = ['users.json', 'auth.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_filter_form(self):
        get_url = reverse('tasks:tasks')
        query_params = {'assignee': 2}
        response = self.client.get(get_url, query_params)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertContains(response, 'Harper Lee')
        self.assertNotContains(response, 'Philip Pullman')

    def test_filter_form_check_box(self):
        get_url = reverse('tasks:tasks')
        query_params = {'personal_tasks': 'on'}
        response = self.client.get(get_url, query_params)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')
        self.assertContains(response, 'Reorganize')
        self.assertContains(response, 'Enhance')
