from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreateForm
from task_manager.users.models import User


class StatusCRUDTestCase(TestCase):
    fixtures = ['user.json', 'auth.json', 'statuses.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_create_status(self):
        post_url = reverse('statuses:create')
        response = self.client.post(post_url, {'name': 'To do'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses:statuses'))
        self.assertEqual(Status.objects.count(), 4)

    def test_create_status_form(self):
        form = StatusCreateForm({'name': 'To do'})
        self.assertTrue(form.is_valid())

    def test_read_statuses(self):
        get_url = reverse('statuses:statuses')
        status = Status.objects.get(pk=1)
        response = self.client.get(get_url)
        response_text = response.content.decode('utf-8')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')
        self.assertIn(status.name, response_text)
        self.assertIn(status, response.context['statuses'])

    def test_update_status(self):
        status = Status.objects.get(name='In progress')
        update_url = reverse('statuses:update', args=[status.pk])
        response = self.client.post(update_url, {'name': 'ASAP'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses:statuses'))
        status.refresh_from_db()
        self.assertEqual(status.name, 'ASAP')

    def test_delete_status(self):
        status = Status.objects.get(name='In progress')
        delete_url = reverse('statuses:delete', args=[status.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('statuses:statuses'))
        self.assertEqual(Status.objects.count(), 2)
