# Generated by Django 4.1.1 on 2023-04-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_doctors', '0003_confirmappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmappointment',
            name='DateOfAppointment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]