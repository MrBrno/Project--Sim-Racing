# Generated by Django 4.0 on 2022-02-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0007_rename_server2_race_remove_server3_car_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, upload_to='car_images'),
        ),
        migrations.AddField(
            model_name='race',
            name='info',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='track',
            name='track_image',
            field=models.ImageField(blank=True, upload_to='track_images'),
        ),
    ]