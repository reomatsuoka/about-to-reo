# Generated by Django 2.2.17 on 2020-12-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201223_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='説明')),
                ('school', models.CharField(max_length=100, verbose_name='学校')),
                ('start', models.CharField(max_length=100, verbose_name='入学')),
                ('graduate', models.CharField(max_length=100, verbose_name='卒業')),
                ('occupation', models.CharField(max_length=100, verbose_name='職業')),
                ('job_place', models.CharField(max_length=100, verbose_name='職場')),
                ('job_period', models.CharField(max_length=100, verbose_name='期間')),
            ],
        ),
    ]