from django.shortcuts import reverse
from django.test import TestCase, RequestFactory

class IndexPageTestCage(TestCase):
    """Test status code of Index Page"""
    def test_index_page_returns_200(self):
        response = self.client.get(reverse('mainapp:index'))
        self.assertEqual(response.status_code, 200)

class AboutPageTestCage(TestCase):
    """Test status code of About Page"""
    def test_about_page_returns_200(self):
        response = self.client.get(reverse('mainapp:about'))
        self.assertEqual(response.status_code, 200)

class StreamersPageTestCage(TestCase):
    """Test status code of Streamers Page"""
    def test_streamers_page_returns_200(self):
        response = self.client.get(reverse('mainapp:streamers'))
        self.assertEqual(response.status_code, 200)

class ContactPageTestCage(TestCase):
    """Test status code of Contact Page"""
    def test_contact_page_returns_200(self):
        response = self.client.get(reverse('mainapp:contact'))
        self.assertEqual(response.status_code, 200)

class GuidesPageTestCage(TestCase):
    """Test status code of Guides Page"""
    def test_guides_page_returns_200(self):
        response = self.client.get(reverse('mainapp:guides'))
        self.assertEqual(response.status_code, 200)

class FAQPageTestCage(TestCase):
    """Test status code of FAQ Page"""
    def test_faq_page_returns_200(self):
        response = self.client.get(reverse('mainapp:faq'))
        self.assertEqual(response.status_code, 200)