# Generated by Django 3.1.6 on 2021-03-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0012_auto_20210308_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
