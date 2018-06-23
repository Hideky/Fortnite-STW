from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.fields import RichTextField
from wagtail.core.signals import page_published
from mainapp.blocks import TwoColumnBlock
from discord import Webhook, RequestsWebhookAdapter, Embed
from datetime import datetime, timedelta
import locale
import os

if os.name == 'nt':
    locale.setlocale(locale.LC_TIME, "fr-FR")
else:
    locale.setlocale(locale.LC_TIME, "fr_FR")

# Create your models here.
class ArticlePage(Page):
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.CharField(max_length=255)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('document', DocumentChooserBlock()),
        ('raw_html', blocks.RawHTMLBlock()),
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        StreamFieldPanel('body'),
    ]

    promote_panels = [
        ImageChooserPanel('feed_image'),
    ]

    @property
    def article_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(ArticlePage, self).get_context(request, *args, **kwargs)
        context['article_page'] = self.article_page
        return context

class GuidePage(Page):
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    description = models.CharField(max_length=255)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
        ('document', DocumentChooserBlock()),
        ('raw_html', blocks.RawHTMLBlock()),
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        StreamFieldPanel('body'),
    ]

    promote_panels = [
        ImageChooserPanel('feed_image'),
    ]

    @property
    def article_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(ArticlePage, self).get_context(request, *args, **kwargs)
        context['article_page'] = self.article_page
        return context

class AnswerPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    @property
    def answer_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(AnswerPage, self).get_context(request, *args, **kwargs)
        context['answer_page'] = self.answer_page
        return context

class HomePage(Page):
    subpage_types = ['ArticlesPage', 'GuidesPage', 'FAQPage']

class ArticlesPage(Page):
    subpage_types = ['ArticlePage']

class GuidesPage(Page):
    subpage_types = ['GuidePage']

class FAQPage(Page):
    subpage_types = ['AnswerPage']

# Let everyone know when a new page is published
def send_to_discord(sender, **kwargs):
    page = kwargs['instance']

    # First published check
    if page.first_published_at != page.last_published_at:
        return
    if page.get_parent().title not in ['Articles']:
        return

    webhook = Webhook.partial(459579353102286859, 'jqaIWsuE0pPhHzrOrGoiNq7P0Y64B4JU5ZdfP7Lmrcpu2mIF6DC8hd3Jv4y9mya0SBqU', adapter=RequestsWebhookAdapter())
    embed = Embed(type="rich", description='{}'.format(page.description), colour=0x90E050)
    embed.set_author(name=page.title, url='{}{}'.format('https://fortnite-stw.fr', page.url), icon_url="https://i.imgur.com/9UsXLG0.png")
    embed.set_thumbnail(url='{}{}'.format('https://fortnite-stw.fr',page.articlepage.feed_image.get_rendition('fill-800x600').url))
    embed.set_footer(text='{} | {}'.format(page.owner.username, (page.first_published_at).strftime('%A %d %B - %H:%M').title()))
    webhook.send(username='Fortnite STW FR', embed=embed)

# Register a receiver
page_published.connect(send_to_discord)