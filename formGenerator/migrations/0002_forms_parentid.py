# Generated by Django 4.0.4 on 2022-04-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formGenerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='parentID',
            field=models.CharField(default=11254512, max_length=500),
        ),
    ]
