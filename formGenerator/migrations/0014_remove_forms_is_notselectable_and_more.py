# Generated by Django 4.0.4 on 2022-04-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formGenerator', '0013_remove_forms_selectlabel_forms_is_notselectable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forms',
            name='is_notselectable',
        ),
        migrations.AlterField(
            model_name='mainform',
            name='InviteKey',
            field=models.TextField(default='cMYrBGkAY7j625AvMjEygY'),
        ),
    ]