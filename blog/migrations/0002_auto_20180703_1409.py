# Generated by Django 2.0.7 on 2018-07-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
    ]
