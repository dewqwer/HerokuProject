# Generated by Django 3.0.6 on 2020-09-05 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200905_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultynewlogic',
            name='requireMeanTime',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]