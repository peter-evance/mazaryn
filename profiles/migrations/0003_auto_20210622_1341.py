# Generated by Django 3.2.4 on 2021-06-22 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_block'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='followee',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Block',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
