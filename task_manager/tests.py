from django.test import TestCase
from django.urls import reverse


class ChangeLanguageTestCase(TestCase):

    def test_language_using_header(self):
        response = self.client.get(reverse('index'), HTTP_ACCEPT_LANGUAGE='ru')
        self.assertContains(response, 'Узнать больше')
