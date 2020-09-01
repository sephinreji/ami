# Generated by Django 3.1 on 2020-08-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_auto_20200825_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traineeprofile',
            name='image',
            field=models.ImageField(default='images/profile.jpg', max_length=255, null=True, upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='trainerprofile',
            name='phone',
            field=models.BigIntegerField(max_length=12, null=True, unique=True),
        ),
    ]