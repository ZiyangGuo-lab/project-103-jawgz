# Generated by Django 2.2.5 on 2019-10-14 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
