# Generated by Django 5.1.5 on 2025-01-31 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_sale_date_sale_date_remove_sale_total_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-date']},
        ),
    ]
