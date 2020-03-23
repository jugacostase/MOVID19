# Generated by Django 2.2 on 2020-03-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covit', '0005_auto_20200322_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='direction',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='destination_activities',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='destination_address',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='home_address',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='ocupation',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='segment',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stop',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]