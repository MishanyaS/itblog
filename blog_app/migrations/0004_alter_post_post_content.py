# Generated by Django 4.1.7 on 2023-04-02 09:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_post_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Post content', null=True),
        ),
    ]
