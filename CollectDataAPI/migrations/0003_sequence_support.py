# Generated by Django 3.2.12 on 2022-04-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CollectDataAPI', '0002_auto_20220422_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='support',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
