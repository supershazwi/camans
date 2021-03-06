# Generated by Django 3.0.1 on 2020-02-23 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adult', '0022_table_database_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nickname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adult.Table')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adult.Worker')),
            ],
        ),
    ]
