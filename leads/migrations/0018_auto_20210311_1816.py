# Generated by Django 3.1.6 on 2021-03-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20210311_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=25),
        ),
    ]
