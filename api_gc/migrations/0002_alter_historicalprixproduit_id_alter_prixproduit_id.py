# Generated by Django 4.2.10 on 2024-03-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalprixproduit',
            name='id',
            field=models.CharField(db_column='id', db_index=True, editable=False, max_length=500, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prixproduit',
            name='id',
            field=models.CharField(db_column='id', editable=False, max_length=500, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
