# Generated by Django 4.0.4 on 2022-05-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_datablog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='datablog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='datablog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]