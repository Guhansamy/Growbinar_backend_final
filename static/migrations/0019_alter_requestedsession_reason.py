# Generated by Django 4.2 on 2024-06-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static', '0018_requestedsession_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedsession',
            name='reason',
            field=models.TextField(),
        ),
    ]