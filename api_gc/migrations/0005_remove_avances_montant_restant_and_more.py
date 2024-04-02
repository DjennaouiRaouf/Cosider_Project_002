# Generated by Django 4.2.10 on 2024-04-02 12:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0004_avances_num_avance_historicalavances_num_avance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avances',
            name='montant_restant',
        ),
        migrations.RemoveField(
            model_name='historicalavances',
            name='montant_restant',
        ),
        migrations.CreateModel(
            name='CumuleAvance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('montant_cumule', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Montant de l'avance")),
                ('montant_restant', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Montant restant de l'avance")),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
