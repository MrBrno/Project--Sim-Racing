# Generated by Django 4.0 on 2022-02-19 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0006_server1_server2_server3_server4_delete_race'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='server2',
            new_name='race',
        ),
        migrations.RemoveField(
            model_name='server3',
            name='car',
        ),
        migrations.RemoveField(
            model_name='server3',
            name='track',
        ),
        migrations.RemoveField(
            model_name='server4',
            name='car',
        ),
        migrations.RemoveField(
            model_name='server4',
            name='track',
        ),
        migrations.DeleteModel(
            name='server1',
        ),
        migrations.DeleteModel(
            name='server3',
        ),
        migrations.DeleteModel(
            name='server4',
        ),
    ]
