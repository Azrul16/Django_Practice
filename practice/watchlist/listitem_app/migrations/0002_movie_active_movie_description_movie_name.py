# Generated by Django 5.1.4 on 2024-12-21 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listitem_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
