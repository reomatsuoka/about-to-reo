# Generated by Django 2.2.17 on 2020-12-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='job_period',
            field=models.CharField(max_length=100, verbose_name='入社'),
        ),
    ]
