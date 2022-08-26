# Generated by Django 4.1 on 2022-08-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_alter_appointment_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='state',
            field=models.CharField(choices=[('Requested', 'requested'), ('Ongoing', 'ongoing'), ('Completed', 'completed')], default='R', max_length=10),
        ),
    ]