# Generated by Django 4.0.4 on 2022-05-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_name_datablog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='datablog',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]