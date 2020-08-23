# Generated by Django 2.2.8 on 2020-08-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200819_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[(1, 'Fashion'), (2, 'Toys'), (3, 'Electronics'), (4, 'Home'), (5, 'Others')], default=5, max_length=1),
        ),
    ]
