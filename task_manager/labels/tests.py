from django.test import TestCase
from django.urls import reverse
from task_manager.custom_utils import load_fixture
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelCreateForm
from django.contrib.auth import get_user_model


class LabelCRUDTestCase(TestCase):
    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        self.user = get_user_model().objects.get(pk=3)
        self.client.force_login(self.user)
        self.labels = load_fixture('labels_to_create.json')

    def test_create_label(self):
        post_url = reverse('labels:create')
        response = self.client.post(post_url, self.labels['debug_label'])

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels:labels'))
        self.assertEqual(Label.objects.count(), 4)

    def test_create_label_form(self):
        form = LabelCreateForm(self.labels['debug_label'])
        self.assertTrue(form.is_valid())

    def test_read_labels(self):
        get_url = reverse('labels:labels')
        label = Label.objects.get(pk=2)
        response = self.client.get(get_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels.html')
        self.assertContains(response, label.name)
        self.assertIn(label, response.context['labels'])

    def test_update_label(self):
        label = Label.objects.get(name='Help needed')
        update_url = reverse('labels:update', args=[label.pk])
        response = self.client.post(update_url, self.labels['undefined_label'])

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels:labels'))
        label.refresh_from_db()
        self.assertEqual(label.name, 'undefined')

    def test_delete_label(self):
        label = Label.objects.get(name='Bug')
        delete_url = reverse('labels:delete', args=[label.pk])
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels:labels'))
        self.assertEqual(Label.objects.all().count(), 2)
