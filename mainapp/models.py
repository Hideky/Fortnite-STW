from django.db import models
from django.conf import settings
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
    """ArticlePage model using to represent any Article on the site"""
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
    """GuidePage model using to represent any Guide on the site"""
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
    def guide_page(self):
        return self.get_parent().specific

    def get_context(self, request, *args, **kwargs):
        context = super(GuidePage, self).get_context(request, *args, **kwargs)
        context['guide_page'] = self.guide_page
        return context

class AnswerPage(Page):
    """AnswerPage model using to represent any Answer in FAQ page on the site"""
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
    """HomePage model using as root directory for the other pages directory"""
    subpage_types = ['ArticlesPage', 'GuidesPage', 'FAQPage']

class ArticlesPage(Page):
    """ArticlesPage model using ArticlePage directory"""
    subpage_types = ['ArticlePage']

class GuidesPage(Page):
    """GuidesPage model using GuidePage directory"""
    subpage_types = ['GuidePage']

class FAQPage(Page):
    """FAQPage model using AnswerPage directory"""
    subpage_types = ['AnswerPage']

def send_to_discord(sender, **kwargs):
    # Let everyone know when a new page is published using Discord Webhook
    page = kwargs['instance']

    # First published check
    if page.first_published_at != page.last_published_at:
        return
    if page.get_parent().title not in ['Articles']:
        return

    webhook = Webhook.partial(settings.DISCORD_WEBHOOK_ID, settings.DISCORD_WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())
    embed = Embed(type="rich", description='{}'.format(page.description), colour=0x90E050)
    embed.set_author(name=page.title, url='https://{}{}'.format(settings.SITE_NAME, page.url), icon_url="https://i.imgur.com/9UsXLG0.png")
    embed.set_thumbnail(url='https://{}{}'.format(settings.SITE_NAME, page.articlepage.feed_image.get_rendition('fill-800x600').url))
    embed.set_footer(text='{} | {}'.format(page.owner.username, (page.first_published_at).strftime('%A %d %B - %H:%M').title()))
    webhook.send(username='Fortnite STW FR', embed=embed)

# Register a receiver
page_published.connect(send_to_discord)