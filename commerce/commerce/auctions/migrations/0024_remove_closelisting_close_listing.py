# Generated by Django 3.2.5 on 2022-06-11 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20220609_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closelisting',
            name='close_listing',
        ),
    ]
