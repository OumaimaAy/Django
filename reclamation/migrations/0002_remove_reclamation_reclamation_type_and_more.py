# Generated by Django 5.1.2 on 2024-10-29 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamation',
            name='reclamation_type',
        ),
        migrations.RemoveField(
            model_name='reclamation',
            name='resolved',
        ),
        migrations.AddField(
            model_name='reclamation',
            name='sentiment',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='reclamation',
            name='title',
            field=models.CharField(default=datetime.date(2025, 1, 1), max_length=255),
            preserve_default=False,
        ),
    ]