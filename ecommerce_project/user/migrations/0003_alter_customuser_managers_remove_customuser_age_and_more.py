# Generated by Django 4.2.16 on 2024-10-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_customuser_age"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="age",
        ),
        migrations.AddField(
            model_name="customuser",
            name="last_active_datetime",
            field=models.DateTimeField(auto_now=True),
        ),
    ]