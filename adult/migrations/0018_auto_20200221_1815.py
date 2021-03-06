# Generated by Django 3.0.1 on 2020-02-21 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adult', '0017_field_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='twid',
            new_name='twid_string',
        ),
        migrations.AlterField(
            model_name='field',
            name='remarks',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='fieldvalue',
            name='remarks',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='role',
            name='remarks',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='table',
            name='remarks',
            field=models.CharField(max_length=10000),
        ),
        migrations.CreateModel(
            name='Twid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twid_card_type', models.CharField(blank=True, max_length=100)),
                ('twid_card_serial_number', models.CharField(blank=True, max_length=100)),
                ('date_twid_card_printed', models.DateTimeField()),
                ('twid_card_printed_by', models.CharField(blank=True, max_length=100)),
                ('date_twid_card_issued', models.DateTimeField()),
                ('twid_card_issued_by', models.CharField(blank=True, max_length=100)),
                ('date_twid_card_withdrawn', models.DateTimeField()),
                ('twid_card_withdrawn_by', models.CharField(blank=True, max_length=100)),
                ('twid_card_remarks', models.CharField(blank=True, max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adult.Worker')),
            ],
        ),
    ]
