# Generated by Django 3.0.6 on 2020-09-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_offline_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='guest',
            field=models.BooleanField(default=False),
        ),
    ]
