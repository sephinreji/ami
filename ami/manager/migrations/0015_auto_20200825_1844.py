# Generated by Django 3.1 on 2020-08-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20200825_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerprofile',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='phone',
            field=models.BigIntegerField(max_length=12, null=True),
        ),
    ]
