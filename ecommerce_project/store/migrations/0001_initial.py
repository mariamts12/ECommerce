# Generated by Django 4.2.16 on 2024-11-08 15:06

import autoslug.fields
import django.core.validators
import django.db.models.deletion
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_en", models.CharField(max_length=100, null=True)),
                ("name_ka", models.CharField(max_length=100, null=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="name", unique=True
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("description_ka", models.TextField(blank=True, null=True)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="categories/"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="store.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("name_en", models.CharField(max_length=50, null=True)),
                ("name_ka", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_en", models.CharField(max_length=100, null=True)),
                ("name_ka", models.CharField(max_length=100, null=True)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False, populate_from="name", unique=True
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("description_ka", models.TextField(blank=True, null=True)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True, null=True, upload_to="products/"
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("category", models.ManyToManyField(to="store.category")),
                (
                    "tag",
                    models.ManyToManyField(related_name="tags", to="store.producttag"),
                ),
            ],
        ),
    ]
