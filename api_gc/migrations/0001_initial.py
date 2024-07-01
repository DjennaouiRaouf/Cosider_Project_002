# Generated by Django 4.2.13 on 2024-07-01 13:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.CharField(db_column='Code_Client', max_length=500, primary_key=True, serialize=False, verbose_name='Code du Client')),
                ('type_client', models.PositiveSmallIntegerField(blank=True, db_column='Type_Client', null=True, verbose_name='Type de Client')),
                ('est_client_cosider', models.BooleanField(blank=True, db_column='Est_Client_Cosider', verbose_name='Est Client Cosider')),
                ('libelle', models.CharField(db_column='Libelle_Client', max_length=300, verbose_name='Libelle')),
                ('adresse', models.CharField(db_column='adresse', max_length=500, verbose_name='Adresse')),
                ('nif', models.CharField(blank=True, db_column='NIF', max_length=50, null=True, unique=True, verbose_name='NIF')),
                ('raison_social', models.CharField(blank=True, db_column='Raison_Social', max_length=50, null=True, verbose_name='Raison Social')),
                ('num_registre_commerce', models.CharField(blank=True, db_column='Num_Registre_Commerce', max_length=20, null=True, verbose_name='Numero du registre de commerce')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('sous_client', models.ForeignKey(blank=True, db_column='sous_client', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.clients', verbose_name='Est client de')),
            ],
            options={
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Clients',
                'db_table': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.CharField(db_column='code_contrat', max_length=500, primary_key=True, serialize=False, verbose_name='Code du contrat')),
                ('libelle', models.CharField(blank=True, db_column='libelle', max_length=500, verbose_name='libelle')),
                ('transport', models.BooleanField(db_column='transport', default=False, verbose_name='Transport')),
                ('rabais', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Rabais')),
                ('rg', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Retenue de garantie')),
                ('date_signature', models.DateField(db_column='date_signature', verbose_name='Date de Signature')),
                ('date_expiration', models.DateField(db_column='date_expiration', null=True, verbose_name="Date d'expiration")),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.clients', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Contrats',
                'verbose_name_plural': 'Contrats',
                'db_table': 'Contrats',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='Images')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Images',
                'verbose_name_plural': 'Images',
                'db_table': 'Images',
            },
        ),
        migrations.CreateModel(
            name='ModePaiement',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=500, unique=True)),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mode de Paiement',
                'verbose_name_plural': 'Mode de Paiement',
                'db_table': 'Mode_De_Paiement',
            },
        ),
        migrations.CreateModel(
            name='Tva',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('valeur', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='TVA')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.CharField(db_column='code_unite', max_length=500, primary_key=True, serialize=False, verbose_name='Code Unité')),
                ('libelle', models.CharField(max_length=500, verbose_name='Libelle')),
                ('date_ouverture', models.DateField(verbose_name="Date d'ouverture")),
                ('date_cloture', models.DateField(blank=True, null=True, verbose_name='Date de cloture')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unités',
                'verbose_name_plural': 'Unités',
                'db_table': 'Unite',
            },
        ),
        migrations.CreateModel(
            name='UniteMesure',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, db_column='libelle', max_length=10, null=True)),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Unités de mesure',
                'verbose_name_plural': 'Unités de mesure',
                'db_table': 'Unite_De_Mesure',
            },
        ),
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.CharField(db_column='code_produits', max_length=500, primary_key=True, serialize=False)),
                ('libelle', models.CharField(blank=True, db_column='nom_produit', max_length=500, verbose_name='Nom Produit')),
                ('famille', models.CharField(db_column='famille', max_length=500, null=True, verbose_name='Famille')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('unite_m', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.unitemesure', verbose_name='Unite de Mesure')),
            ],
            options={
                'verbose_name': 'Produits',
                'verbose_name_plural': 'Produits',
                'db_table': 'Produit',
            },
        ),
        migrations.CreateModel(
            name='PrixProduit',
            fields=[
                ('id', models.CharField(db_column='id', editable=False, max_length=500, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_unitaire', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prix unitaire')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.produits', verbose_name='Produit')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.unite', verbose_name='unite')),
            ],
            options={
                'verbose_name': 'Prix des Produits',
                'verbose_name_plural': 'Prix des Produits',
                'db_table': 'Prix_Produit',
                'unique_together': {('produit', 'prix_unitaire')},
            },
        ),
        migrations.CreateModel(
            name='Factures',
            fields=[
                ('id', models.CharField(editable=False, max_length=500, primary_key=True, serialize=False, verbose_name='Numero de facture')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('du', models.DateField(verbose_name='Du')),
                ('au', models.DateField(verbose_name='Au')),
                ('paye', models.BooleanField(default=False, editable=False)),
                ('montant', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant')),
                ('montant_rb', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant Rabais')),
                ('montant_rg', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant RG')),
                ('montant_facture_ht', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant Facture (en HT)')),
                ('montant_facture_ttc', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant Facture (en TTC)')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
            ],
            options={
                'verbose_name': 'Factures',
                'verbose_name_plural': 'Factures',
                'db_table': 'Factures',
            },
        ),
        migrations.CreateModel(
            name='DQE',
            fields=[
                ('id', models.CharField(editable=False, max_length=500, primary_key=True, serialize=False, verbose_name='id')),
                ('qte', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité')),
                ('prix_transport', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tarif de Transport')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
                ('prixProduit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.prixproduit', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'DQE',
                'verbose_name_plural': 'DQE',
                'db_table': 'DQE',
            },
        ),
        migrations.AddField(
            model_name='contrat',
            name='tva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.tva', verbose_name='TVA'),
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saisie_automatique', models.BooleanField(default=False, verbose_name='Saisie Automatique')),
                ('port', models.CharField(default='COM1', max_length=500, verbose_name='Port')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('unite', models.ForeignKey(blank=True, db_column='unite', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.unite', verbose_name='Unite')),
            ],
            options={
                'verbose_name': 'Config',
                'verbose_name_plural': 'Config',
                'db_table': 'Config',
            },
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('matricule', models.CharField(max_length=500, primary_key=True, serialize=False, verbose_name='Matricule')),
                ('tare', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tare')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('unite', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.unitemesure', verbose_name='Unite de Mesure')),
            ],
            options={
                'verbose_name': 'Camions',
                'verbose_name_plural': 'Camions',
                'db_table': 'Camions',
            },
        ),
        migrations.CreateModel(
            name='BonLivraison',
            fields=[
                ('id', models.CharField(editable=False, max_length=500, primary_key=True, serialize=False, verbose_name='N° BL')),
                ('conducteur', models.CharField(max_length=500, verbose_name='Conducteur')),
                ('numero_permis_c', models.CharField(max_length=500, null=True, verbose_name='N° P.Conduire')),
                ('date', models.DateTimeField(auto_now=True)),
                ('ptc', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='PTC')),
                ('montant', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant')),
                ('qte', models.DecimalField(decimal_places=3, default=0, editable=False, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='QTE')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.camion', verbose_name='Camion')),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
                ('dqe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.dqe', verbose_name='dqe')),
            ],
            options={
                'verbose_name': 'Bon de livraison',
                'verbose_name_plural': 'Bon de livraison',
                'db_table': 'Bon_De_Livraison',
            },
        ),
        migrations.CreateModel(
            name='Avances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_avance', models.PositiveIntegerField(default=0, editable=False, verbose_name='Num avance')),
                ('montant_avance', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Montant de l'avance")),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
            ],
            options={
                'verbose_name': 'Avances',
                'verbose_name_plural': 'Avances',
                'db_table': 'Avances',
                'unique_together': {('contrat', 'montant_avance')},
            },
        ),
        migrations.CreateModel(
            name='Planing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('qte_livre', models.DecimalField(decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantité à livré')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.contrat', verbose_name='Contrat')),
                ('dqe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.dqe', verbose_name='dqe')),
            ],
            options={
                'verbose_name': 'Planing',
                'verbose_name_plural': 'Planing',
                'db_table': 'Planing',
                'unique_together': {('contrat', 'dqe', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Encaissement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_encaissement', models.DateField(verbose_name="Date d'encaissement")),
                ('montant_encaisse', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=38, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Montant encaissé')),
                ('numero_piece', models.CharField(max_length=300, verbose_name='Numero de piéce')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('avance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.avances', verbose_name='Avance')),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.factures', verbose_name='Facture')),
                ('mode_paiement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.modepaiement', verbose_name='Mode de paiement')),
            ],
            options={
                'verbose_name': 'Encaissements',
                'verbose_name_plural': 'Encaissements',
                'db_table': 'Encaissements',
                'unique_together': {('facture', 'date_encaissement')},
            },
        ),
        migrations.CreateModel(
            name='DetailFacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_bloquer', models.BooleanField(default=False, editable=False)),
                ('user_id', models.CharField(editable=False, max_length=500)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.bonlivraison')),
                ('facture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_gc.factures')),
            ],
            options={
                'verbose_name': 'Details',
                'verbose_name_plural': 'Details',
                'db_table': 'Details',
                'unique_together': {('facture', 'detail')},
            },
        ),
    ]
