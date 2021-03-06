# Generated by Django 2.2.3 on 2019-07-29 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pari', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiquet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero1', models.CharField(max_length=10)),
                ('numero2', models.CharField(max_length=10)),
                ('mise', models.CharField(max_length=150)),
                ('datepari', models.DateTimeField(default=django.utils.timezone.now)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
