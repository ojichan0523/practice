# Generated by Django 4.2.1 on 2023-06-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="url",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
