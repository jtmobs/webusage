# Generated by Django 3.2.12 on 2022-04-22 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CollectDataAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequenceidentifier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webpageidentifierwebpage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
