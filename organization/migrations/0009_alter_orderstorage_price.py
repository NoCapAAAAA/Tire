# Generated by Django 4.0.5 on 2023-04-13 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_alter_orderstorage_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstorage',
            name='price',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
