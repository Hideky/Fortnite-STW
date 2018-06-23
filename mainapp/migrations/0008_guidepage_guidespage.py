# Generated by Django 2.0.6 on 2018-06-23 00:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailcore', '0040_page_draft_title'),
        ('mainapp', '0007_answerpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.CharField(max_length=255)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('rawhtml', wagtail.core.blocks.RawHTMLBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())], icon='arrow-right', label='Right column content'))])), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GuidesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
