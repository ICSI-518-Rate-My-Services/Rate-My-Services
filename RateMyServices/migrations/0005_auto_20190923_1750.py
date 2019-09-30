# Generated by Django 2.2.5 on 2019-09-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RateMyServices', '0004_auto_20190920_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_type',
            new_name='service',
        ),
        migrations.AlterField(
            model_name='generaluser',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='generaluser',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='generaluser',
            name='zips',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.DeleteModel(
            name='Zip',
        ),
    ]
