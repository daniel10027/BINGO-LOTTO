# Generated by Django 2.2.3 on 2019-07-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pari', '0005_auto_20190729_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiquet',
            name='event',
            field=models.CharField(default='national', max_length=150),
        ),
    ]
