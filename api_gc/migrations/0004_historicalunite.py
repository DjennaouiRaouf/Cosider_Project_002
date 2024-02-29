# Generated by Django 4.2.10 on 2024-02-28 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_gc', '0003_alter_unite_date_cloture'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUnite',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.CharField(db_column='code_unite', db_index=True, max_length=500, verbose_name='Code Unité')),
                ('libelle', models.CharField(max_length=500, verbose_name='Libelle')),
                ('date_ouverture', models.DateField(verbose_name="Date d'ouverture")),
                ('date_cloture', models.DateField(blank=True, null=True, verbose_name='Date de cloture')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical unite',
                'verbose_name_plural': 'historical unites',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]