# Generated by Django 4.2.4 on 2023-08-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0002_remove_veisle_iranga_remove_veisle_vietove_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veisle',
            name='siltnamis_ar_laukas',
            field=models.CharField(choices=[('siltnamis', 'siltnamis'), ('laukas', 'laukas')], default='siltnamis', max_length=10),
        ),
    ]