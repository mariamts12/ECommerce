# Generated by Django 4.2.16 on 2024-10-23 15:13

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
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
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to="products/"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tag",
            field=models.ManyToManyField(related_name="tags", to="store.producttag"),
        ),
    ]