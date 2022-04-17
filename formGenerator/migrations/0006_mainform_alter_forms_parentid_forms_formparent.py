# Generated by Django 4.0.4 on 2022-04-16 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formGenerator', '0005_formstore_alter_forms_parentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('InviteKey', models.TextField(default='CdEzVWQArswLx6TXrXoGcL')),
            ],
        ),
        migrations.AlterField(
            model_name='forms',
            name='parentID',
            field=models.CharField(default=75019108, max_length=500),
        ),
        migrations.AddField(
            model_name='forms',
            name='formParent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='formGenerator.mainform'),
        ),
    ]