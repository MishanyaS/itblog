# Generated by Django 4.1.7 on 2023-05-30 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_alter_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('post_title', 'post_content')},
        ),
    ]