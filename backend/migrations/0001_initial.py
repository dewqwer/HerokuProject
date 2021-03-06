# Generated by Django 2.2.12 on 2020-09-19 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountRealTime',
            fields=[
                ('countID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('round', models.PositiveIntegerField(null=True)),
                ('peopleCount', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'count_real_time',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyID', models.AutoField(primary_key=True, serialize=False)),
                ('facultyName', models.CharField(max_length=40)),
                ('peopleInFaculty', models.PositiveIntegerField()),
                ('university', models.CharField(max_length=40)),
                ('queueFaculty', models.PositiveIntegerField()),
                ('queueFacultyPassed', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('majorID', models.AutoField(primary_key=True, serialize=False)),
                ('typeDegree', models.CharField(max_length=40)),
                ('majorName', models.CharField(max_length=40)),
                ('peopleInMajor', models.PositiveIntegerField()),
                ('queueMajor', models.PositiveIntegerField()),
                ('queueMajorPassed', models.BooleanField(null=True)),
                ('facultyID', models.ForeignKey(db_column='faculty_facultyID', null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Faculty')),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='timeMajor',
            fields=[
                ('timeID', models.AutoField(primary_key=True, serialize=False)),
                ('timeStart', models.TimeField(blank=True, null=True)),
                ('timeStop', models.TimeField(blank=True, null=True)),
                ('timeExpect', models.TimeField(blank=True, null=True)),
                ('requireMeanTime', models.PositiveIntegerField(null=True)),
                ('speed', models.CharField(blank=True, choices=[('OK', 'OK'), ('NOT OK', 'NOT OK')], max_length=40, null=True)),
                ('majorID', models.ForeignKey(db_column='major_majorID', null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Major')),
            ],
            options={
                'db_table': 'time_major',
            },
        ),
        migrations.CreateModel(
            name='GraduationDetail',
            fields=[
                ('detailID', models.AutoField(primary_key=True, serialize=False)),
                ('academinYear', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('typeCeremony', models.BooleanField()),
                ('round', models.PositiveIntegerField(null=True)),
                ('place', models.CharField(blank=True, max_length=40, null=True)),
                ('facultyID', models.ForeignKey(db_column='faculty_facultyID', null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Faculty')),
            ],
            options={
                'db_table': 'graduation_detail',
            },
        ),
    ]
