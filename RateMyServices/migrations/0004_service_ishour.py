# Generated by Django 2.2.5 on 2019-11-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RateMyServices', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='isHour',
            field=models.BooleanField(default=False),
        ),
    ]
