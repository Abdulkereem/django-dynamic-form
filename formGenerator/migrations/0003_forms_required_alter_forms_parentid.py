# Generated by Django 4.0.4 on 2022-04-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formGenerator', '0002_forms_parentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='forms',
            name='parentID',
            field=models.CharField(default=43612713, max_length=500),
        ),
    ]
