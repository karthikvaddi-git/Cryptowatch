# Generated by Django 3.2.10 on 2021-12-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoapp', '0002_cointracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='cointracker',
            name='messagesent',
            field=models.BooleanField(default=False),
        ),
    ]
