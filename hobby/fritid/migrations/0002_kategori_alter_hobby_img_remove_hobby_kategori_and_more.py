# Generated by Django 4.0.4 on 2022-05-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fritid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='hobby',
            name='img',
            field=models.ImageField(upload_to='menu_images/'),
        ),
        migrations.RemoveField(
            model_name='hobby',
            name='kategori',
        ),
        migrations.AlterField(
            model_name='hobby',
            name='pris',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.CreateModel(
            name='SlagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('pris', models.DecimalField(decimal_places=2, max_digits=7)),
                ('items', models.ManyToManyField(blank=True, null=True, related_name='slags', to='fritid.hobby')),
            ],
        ),
        migrations.AddField(
            model_name='hobby',
            name='kategori',
            field=models.ManyToManyField(related_name='item', to='fritid.kategori'),
        ),
    ]
