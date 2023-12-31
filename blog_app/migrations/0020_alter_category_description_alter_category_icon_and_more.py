# Generated by Django 4.1.7 on 2023-06-21 07:45

import blog_app.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_remove_post_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, validators=[blog_app.models.validate_description_for_category]),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='category_icons/', validators=[blog_app.models.validate_icon_for_category]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, validators=[blog_app.models.validate_name_for_category]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, validators=[blog_app.models.validate_comment_content_for_comment]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, validators=[blog_app.models.validate_name_for_comment]),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.CharField(default='programming', max_length=200, validators=[blog_app.models.validate_post_category_for_post]),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, validators=[blog_app.models.validate_post_content_for_post]),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/posts', validators=[blog_app.models.validate_post_image_for_post]),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=200, validators=[blog_app.models.validate_post_title_for_post]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[blog_app.models.validate_phone_for_profile]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_birth_date',
            field=models.DateField(blank=True, null=True, validators=[blog_app.models.validate_user_birth_date_for_profile]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_description',
            field=models.TextField(blank=True, null=True, validators=[blog_app.models.validate_user_description_for_profile]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_github_url',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[blog_app.models.validate_user_github_url_for_profile]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_link',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[blog_app.models.validate_user_link_for_profile]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/', validators=[blog_app.models.validate_user_photo_for_profile]),
        ),
    ]
