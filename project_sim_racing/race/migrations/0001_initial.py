# Generated by Django 4.0 on 2022-02-22 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=50)),
                ('model_name', models.CharField(default='', max_length=50)),
                ('car_image', models.ImageField(blank=True, upload_to='car_images')),
                ('in_game_name', models.CharField(default='ks_', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(default='', max_length=50)),
                ('track_image', models.ImageField(blank=True, upload_to='track_images')),
            ],
        ),
        migrations.CreateModel(
            name='race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_server', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('info', models.TextField(default='', max_length=500)),
                ('minute', models.IntegerField()),
                ('mod_link', models.CharField(blank=True, default='', max_length=1000)),
                ('practice_time', models.IntegerField(default=5)),
                ('quaulify_time', models.IntegerField(default=10)),
                ('race_laps', models.IntegerField(default=5)),
                ('server_ip', models.CharField(default='195.211.11.141', max_length=20)),
                ('port_number', models.IntegerField(default=8080)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.track')),
            ],
        ),
        migrations.CreateModel(
            name='cars_for_the_race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.car')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.race')),
            ],
        ),
    ]
