# Generated by Django 4.2.10 on 2024-03-04 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0004_remove_bonlivraison_qte_cumule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonlivraison',
            name='montant_mois',
        ),
        migrations.RemoveField(
            model_name='historicalbonlivraison',
            name='montant_mois',
        ),
    ]