# Generated by Django 4.2 on 2024-05-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('static', '0012_authtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('from_email', models.EmailField(max_length=254)),
                ('to_email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('query', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static.mentee')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static.mentor')),
            ],
        ),
    ]
