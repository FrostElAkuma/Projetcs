# Generated by Django 3.2.5 on 2021-08-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_listing_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.URLField(blank=True),
        ),
    ]
