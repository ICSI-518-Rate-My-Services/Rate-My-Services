# Generated by Django 2.2.5 on 2019-10-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RateMyServices', '0013_advertisment_userimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='rate',
            field=models.CharField(max_length=30),
        ),
    ]
