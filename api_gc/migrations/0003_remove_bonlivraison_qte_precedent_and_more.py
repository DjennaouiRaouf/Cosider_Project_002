# Generated by Django 4.2.10 on 2024-03-04 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0002_remove_historicalplaning_qte_cumule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonlivraison',
            name='qte_precedent',
        ),
        migrations.RemoveField(
            model_name='historicalbonlivraison',
            name='qte_precedent',
        ),
    ]