# Generated by Django 4.1 on 2022-08-26 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Non-Binary')], max_length=2)),
                ('birthday', models.DateField(null=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('mobile_no', models.CharField(max_length=14)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('license_no', models.CharField(max_length=10)),
                ('specialist', models.CharField(max_length=20)),
                ('verified', models.CharField(choices=[('verified', 'verified'), ('pending', 'pending'), ('rejected', 'rejected')], max_length=10)),
                ('prescriptionFields', models.CharField(default='NAME#AGE#SEX#PROBLEM DESCRIPTION#DIAGNOSIS#TEST', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DegreeOfDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=20)),
                ('institute', models.CharField(blank=True, max_length=30)),
                ('degree_date', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sat_starttime', models.TimeField(null=True)),
                ('sat_endtime', models.TimeField(null=True)),
                ('sun_starttime', models.TimeField(null=True)),
                ('sun_endtime', models.TimeField(null=True)),
                ('mon_starttime', models.TimeField(null=True)),
                ('mon_endtime', models.TimeField(null=True)),
                ('tues_starttime', models.TimeField(null=True)),
                ('tues_endtime', models.TimeField(null=True)),
                ('wed_starttime', models.TimeField(null=True)),
                ('wed_endtime', models.TimeField(null=True)),
                ('thrs_starttime', models.TimeField(null=True)),
                ('thrs_endtime', models.TimeField(null=True)),
                ('fri_starttime', models.TimeField(null=True)),
                ('fri_endtime', models.TimeField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('payment', models.IntegerField()),
                ('max_capacity', models.IntegerField(default=3)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('state', models.CharField(choices=[('Requested', 'Requested'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Requested', max_length=10)),
                ('otp', models.IntegerField(blank=True, default=1111, null=True)),
                ('prescription', models.CharField(blank=True, max_length=500, null=True)),
                ('chamber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.chamber')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
