# Generated by Django 3.1.2 on 2020-10-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salasah', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
