# Generated by Django 4.0.4 on 2022-04-17 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('point_depart', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('altitude_depart', models.IntegerField()),
                ('altitude_min', models.IntegerField()),
                ('altitude_max', models.IntegerField()),
                ('denivele_neg', models.IntegerField()),
                ('denivele_pos', models.IntegerField()),
                ('duree_estimee', models.IntegerField()),
                ('difficulte_estimee', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
