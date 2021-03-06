# Generated by Django 4.0.2 on 2022-02-18 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0005_race_port_number_race_server_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='server1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_server', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('minute', models.IntegerField()),
                ('practice_time', models.IntegerField(default=5)),
                ('qualify_time', models.IntegerField(default=10)),
                ('race_laps', models.IntegerField(default=5)),
                ('server_ip', models.CharField(default='195.211.11.141', max_length=20)),
                ('port_number', models.IntegerField(default=8080)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.car')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.track')),
            ],
        ),
        migrations.CreateModel(
            name='server2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_server', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('minute', models.IntegerField()),
                ('practice_time', models.IntegerField(default=5)),
                ('quaulify_time', models.IntegerField(default=10)),
                ('race_laps', models.IntegerField(default=5)),
                ('server_ip', models.CharField(default='195.211.11.141', max_length=20)),
                ('port_number', models.IntegerField(default=8080)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.car')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.track')),
            ],
        ),
        migrations.CreateModel(
            name='server3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_server', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('minute', models.IntegerField()),
                ('practice_time', models.IntegerField(default=5)),
                ('quaulify_time', models.IntegerField(default=10)),
                ('race_laps', models.IntegerField(default=5)),
                ('server_ip', models.CharField(default='195.211.11.141', max_length=20)),
                ('port_number', models.IntegerField(default=8080)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.car')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.track')),
            ],
        ),
        migrations.CreateModel(
            name='server4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_server', models.BooleanField(default=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('minute', models.IntegerField()),
                ('practice_time', models.IntegerField(default=5)),
                ('quaulify_time', models.IntegerField(default=10)),
                ('race_laps', models.IntegerField(default=5)),
                ('server_ip', models.CharField(default='195.211.11.141', max_length=20)),
                ('port_number', models.IntegerField(default=8080)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.car')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='race.track')),
            ],
        ),
        migrations.DeleteModel(
            name='Race',
        ),
    ]
