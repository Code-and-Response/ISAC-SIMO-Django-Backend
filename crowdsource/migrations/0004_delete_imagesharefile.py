# Generated by Django 3.2.4 on 2021-07-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsource', '0003_imageshare_imagesharefile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageShareFile',
        ),
    ]