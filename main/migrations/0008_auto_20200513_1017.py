# Generated by Django 3.0.6 on 2020-05-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200509_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventservice',
            name='event_type',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Concert', 'Concert')], max_length=10),
        ),
    ]
