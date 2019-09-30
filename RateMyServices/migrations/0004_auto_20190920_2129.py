# Generated by Django 2.2.5 on 2019-09-20 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RateMyServices', '0003_auto_20190912_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generalUserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateMyServices.GeneralUser')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('professionalUserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateMyServices.ProfessionalUser')),
            ],
        ),
        migrations.AlterField(
            model_name='rating',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateMyServices.ProfessionalUser'),
        ),
        migrations.AlterField(
            model_name='service',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RateMyServices.ProfessionalUser'),
        ),
        migrations.DeleteModel(
            name='ProfessinalUser',
        ),
    ]
