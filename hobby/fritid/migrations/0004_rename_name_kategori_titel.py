# Generated by Django 4.0.4 on 2022-05-13 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0003_alter_slagsmodel_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategori',
            old_name='name',
            new_name='titel',
        ),
    ]