# Generated by Django 4.2.16 on 2024-10-30 08:58

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to="categories/"
            ),
        ),
    ]