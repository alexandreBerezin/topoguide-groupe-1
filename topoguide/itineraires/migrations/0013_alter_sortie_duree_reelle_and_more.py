# Generated by Django 4.0.4 on 2022-05-04 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0012_merge_0003_map_0011_commentaire_cache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortie',
            name='duree_reelle',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sortie',
            name='nombre_participants',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
