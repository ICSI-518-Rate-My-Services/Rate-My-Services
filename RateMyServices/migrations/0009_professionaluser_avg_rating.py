# Generated by Django 2.2.5 on 2019-09-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RateMyServices', '0008_professionaluser_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionaluser',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
