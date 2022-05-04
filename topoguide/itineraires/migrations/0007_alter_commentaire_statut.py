# Generated by Django 4.0.4 on 2022-05-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0006_alter_commentaire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='statut',
            field=models.CharField(choices=[('PB', 'Public'), ('PR', 'Privé'), ('CA', 'Caché')], default='PB', max_length=2),
        ),
    ]
