# Generated by Django 4.2.10 on 2024-03-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0013_remove_contrat_validite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrat',
            name='_validite_mois',
            field=models.IntegerField(default=0, verbose_name='Durée de validité (en Mois)'),
        ),
        migrations.AddField(
            model_name='historicalcontrat',
            name='_validite_mois',
            field=models.IntegerField(default=0, verbose_name='Durée de validité (en Mois)'),
        ),
    ]