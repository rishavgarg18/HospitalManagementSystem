# Generated by Django 2.0 on 2020-06-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorbasicdetail',
            name='degree',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
