# Generated by Django 2.0 on 2020-06-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_doctorbasicdetail_previous_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorbasicdetail',
            name='status',
            field=models.CharField(default='NOT APPROVED', max_length=50),
        ),
    ]
