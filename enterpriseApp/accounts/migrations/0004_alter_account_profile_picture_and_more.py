# Generated by Django 5.1.1 on 2024-10-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, default='users/profile_pics/80x80.png', null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='users/profile_pics/300x150.png', upload_to='users/profile_pictures'),
        ),
    ]
