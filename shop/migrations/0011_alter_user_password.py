# Generated by Django 5.1.3 on 2024-11-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_supportmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
