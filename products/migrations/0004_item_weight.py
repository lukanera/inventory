# Generated by Django 5.1.6 on 2025-03-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]
