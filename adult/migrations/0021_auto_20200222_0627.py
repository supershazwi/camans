# Generated by Django 3.0.1 on 2020-02-22 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adult', '0020_twid_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twid',
            name='identifier',
        ),
        migrations.AddField(
            model_name='twid',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adult.Table'),
        ),
    ]
