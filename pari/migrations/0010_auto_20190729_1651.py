# Generated by Django 2.2.3 on 2019-07-29 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pari', '0009_lotterie_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiquet',
            old_name='event',
            new_name='Lotterie',
        ),
    ]