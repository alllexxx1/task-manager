from django.test import TestCase
from django.urls import reverse


class ChangeLanguageTestCase(TestCase):

    def test_various_language_using_header(self):
        response = self.client.get(reverse('index'), HTTP_ACCEPT_LANGUAGE='ru')
        self.assertContains(response, 'Узнать больше')

        response = self.client.get(reverse('index'), HTTP_ACCEPT_LANGUAGE='en')
        self.assertContains(response, 'Learn more...')

    def test_test(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Вход')
