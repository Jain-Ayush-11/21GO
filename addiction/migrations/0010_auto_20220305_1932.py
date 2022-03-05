# Generated by Django 3.2.10 on 2022-03-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addiction', '0009_achievements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievements',
            name='is_unlocked',
        ),
        migrations.RemoveField(
            model_name='achievements',
            name='name',
        ),
        migrations.AlterField(
            model_name='achievements',
            name='attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='achievements',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]