# Generated by Django 3.1.6 on 2021-03-08 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20210308_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='description',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='email',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='phone_number',
        ),
    ]
