from django.shortcuts import reverse
from django.test import TestCase, RequestFactory
from wagtail.tests.utils import WagtailPageTests
from wagtail.tests.utils.form_data import nested_form_data, streamfield, rich_text
from wagtail.core.models import Page
from .models import HomePage, ArticlesPage, ArticlePage, GuidesPage, GuidePage, FAQPage, AnswerPage

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

class IndexPageTests(WagtailPageTests):
    def test_can_create_under_home_page(self):
        """Test if ArticlesPage, GuidesPage and FAQ can be create under a HomePage"""
        self.assertAllowedSubpageTypes(HomePage, {ArticlesPage, GuidesPage, FAQPage})

class ArticlesPageTests(WagtailPageTests):
    def test_can_create_under_articles_page(self):
        """Test if ArticlePage can be create under a ArticlesPage"""
        self.assertCanCreateAt(ArticlesPage, ArticlePage)

    def test_can_create_article_page(self):
        # Get the HomePage
        root_page = Page.objects.get(id=1)
    
        # Test if ArticlesPage can be create
        self.assertCanCreate(root_page, ArticlesPage, nested_form_data({
            'title': 'Articles'
        }))

        # Get the ArticlesPage created previously
        root_page = ArticlesPage.objects.get(title='Articles')

        # Test if ArticlePage can be create
        self.assertCanCreate(root_page, ArticlePage, nested_form_data({
            'title': 'Articles',
            'description': 'Lorem ipsum dolor',
            'body': streamfield([
                ('text', 'Lorem ipsum dolor sit amet'),
            ])
        }))

class GuidePageTests(WagtailPageTests):
    def test_can_create_under_guides_page(self):
        """Test if GuidePage can be create under a GuidesPage"""
        self.assertCanCreateAt(GuidesPage, GuidePage)

    def test_can_create_guide_page(self):
        # Get the HomePage
        root_page = Page.objects.get(id=1)
    
        # Test if GuidesPage can be create
        self.assertCanCreate(root_page, GuidesPage, nested_form_data({
            'title': 'Guides'
        }))

        # Get the GuidesPage created previously
        root_page = GuidesPage.objects.get(title='Guides')

        # Test if GuidePage can be create
        self.assertCanCreate(root_page, GuidePage, nested_form_data({
            'title': 'Guides',
            'description': 'Lorem ipsum dolor',
            'body': streamfield([
                ('text', 'Lorem ipsum dolor sit amet'),
            ])
        }))


class FAQPageTests(WagtailPageTests):
    def test_can_create_under_faq_page(self):
        """Test if AnswerPage can be create under a FAQPage"""
        self.assertCanCreateAt(FAQPage, AnswerPage)

    def test_can_create_answer_page(self):
        # Get the HomePage
        root_page = Page.objects.get(id=1)
    
        # Test if FAQPage can be create
        self.assertCanCreate(root_page, FAQPage, nested_form_data({
            'title': 'FAQ'
        }))

        # Get the FAQPage created previously
        root_page = FAQPage.objects.get(title='FAQ')

        # Test if AnswerPage can be create
        self.assertCanCreate(root_page, AnswerPage, nested_form_data({
            'title': 'How to Lorem ipsum',
            'body': rich_text('<p>Lorem ipsum dolor sit amet</p>')
        }))
