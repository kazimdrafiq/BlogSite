# Generated by Django 4.0.4 on 2022-05-29 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_datablog_category_alter_datablog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datablog',
            old_name='message',
            new_name='descriptions',
        ),
    ]
