# Generated by Django 2.2.12 on 2020-09-12 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20200906_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountRealTimeNewLogic',
            fields=[
                ('countID', models.AutoField(primary_key=True, serialize=False)),
                ('numOfCount', models.IntegerField()),
                ('detailID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.GraduationDetail')),
            ],
        ),
    ]
