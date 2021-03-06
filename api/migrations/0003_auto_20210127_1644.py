# Generated by Django 3.1.5 on 2021-01-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210125_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='athlete_team',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='game',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='noc',
            name='notes',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='noc',
            name='region',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]