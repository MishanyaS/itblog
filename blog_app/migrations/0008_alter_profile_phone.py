# Generated by Django 4.1.7 on 2023-05-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_profile_phone_alter_profile_user_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, help_text='Phone', max_length=200, null=True),
        ),
    ]
