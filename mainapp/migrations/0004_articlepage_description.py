# Generated by Django 2.0.6 on 2018-06-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_articlepage_feed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='description',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
