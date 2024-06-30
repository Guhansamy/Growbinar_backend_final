# Generated by Django 4.2 on 2024-05-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static', '0008_mentee_languages_session_count_of_sessions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='profile_picture_url',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='profile_picture_url',
            field=models.CharField(blank=True, null=True),
        ),
    ]