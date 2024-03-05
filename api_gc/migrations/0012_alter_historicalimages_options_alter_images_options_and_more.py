# Generated by Django 4.2.10 on 2024-03-04 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_gc', '0011_alter_historicalimages_itemimagesrc_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalimages',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Images', 'verbose_name_plural': 'historical Images'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Images', 'verbose_name_plural': 'Images'},
        ),
        migrations.RenameField(
            model_name='historicalimages',
            old_name='itemImageSrc',
            new_name='src',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='itemImageSrc',
            new_name='src',
        ),
        migrations.RemoveField(
            model_name='historicalimages',
            name='alt',
        ),
        migrations.RemoveField(
            model_name='historicalimages',
            name='thumbnailImageSrc',
        ),
        migrations.RemoveField(
            model_name='historicalimages',
            name='title',
        ),
        migrations.RemoveField(
            model_name='images',
            name='alt',
        ),
        migrations.RemoveField(
            model_name='images',
            name='thumbnailImageSrc',
        ),
        migrations.RemoveField(
            model_name='images',
            name='title',
        ),
    ]
