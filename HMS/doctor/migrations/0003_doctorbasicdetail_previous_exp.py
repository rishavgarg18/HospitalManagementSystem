# Generated by Django 2.0 on 2020-06-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctorbasicdetail_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorbasicdetail',
            name='previous_exp',
            field=models.IntegerField(null=True),
        ),
    ]
