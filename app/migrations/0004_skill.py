# Generated by Django 2.2.17 on 2020-12-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_education_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('level', models.IntegerField(verbose_name='スキルレベル')),
            ],
        ),
    ]
