# Generated by Django 2.2.3 on 2019-07-29 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pari', '0004_auto_20190729_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiquet',
            old_name='joueur',
            new_name='recu',
        ),
    ]
