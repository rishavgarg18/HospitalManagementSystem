# Generated by Django 2.0 on 2020-06-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20200615_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_date',
            field=models.CharField(max_length=100),
        ),
    ]