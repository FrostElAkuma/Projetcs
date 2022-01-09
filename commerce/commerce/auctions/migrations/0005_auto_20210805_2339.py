# Generated by Django 3.2.5 on 2021-08-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210805_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='watchList',
        ),
        migrations.AddField(
            model_name='watch',
            name='watchList',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchers', to='auctions.listing'),
        ),
    ]
