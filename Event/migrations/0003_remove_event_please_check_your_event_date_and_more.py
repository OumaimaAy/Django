# Generated by Django 4.2 on 2024-10-29 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0002_remove_event_please_check_your_event_date_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='Please check your event date',
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('evt_date__gt', datetime.datetime(2024, 10, 29, 16, 48, 5, 88764))), name='Please check your event date'),
        ),
    ]
