# Generated by Django 4.2.10 on 2024-03-25 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factures',
            old_name='numero_facture',
            new_name='id',
        ),
    ]