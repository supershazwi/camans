# Generated by Django 3.0.1 on 2020-02-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adult', '0018_auto_20200221_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='subsidiary_to',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]