# Generated by Django 2.2.5 on 2019-10-13 23:58

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=200)),
                ('vehicle_model', models.CharField(max_length=200)),
                ('location_to', models.CharField(max_length=200)),
                ('location_from', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=post.models.default_datetime)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
