from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse


class HomePageTest(SimpleTestCase):
    """
        Test for the response of Home Page
    """
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_name(self):
        response = self.client.get(reverse('schema-swagger-ui'))
        self.assertEqual(response.status_code, 200)
