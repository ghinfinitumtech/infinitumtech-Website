# Generated by Django 5.0.3 on 2024-10-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerapplication',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]