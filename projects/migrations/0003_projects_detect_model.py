# Generated by Django 2.0 on 2020-04-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200407_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='detect_model',
            field=models.TextField(blank=True, null=True),
        ),
    ]