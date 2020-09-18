# Generated by Django 3.0.6 on 2020-09-05 16:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200905_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultynewlogic',
            name='queueFaculty',
            field=models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0)),
        ),
        migrations.AlterField(
            model_name='facultynewlogic',
            name='requireMeanTime',
            field=models.FloatField(verbose_name=django.core.validators.MinValueValidator(0)),
        ),
    ]
