# Generated by Django 4.0.4 on 2022-05-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0006_slagsmodel_by_slagsmodel_email_slagsmodel_navn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='/menu_images/'),
        ),
    ]