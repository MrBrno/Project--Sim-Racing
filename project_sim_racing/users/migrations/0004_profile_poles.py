# Generated by Django 4.0 on 2022-02-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_laps_lead_profile_podiums_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='poles',
            field=models.IntegerField(default='0'),
        ),
    ]
