# Generated by Django 4.2.10 on 2024-04-02 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailfacture',
            name='facture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.factures'),
        ),
    ]