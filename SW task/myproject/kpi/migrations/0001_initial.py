# Generated by Django 5.1.2 on 2024-10-29 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="KPI",
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
                ("expression", models.TextField()),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AssetKPI",
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
                ("asset_id", models.CharField(max_length=50)),
                (
                    "kpi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kpi.kpi"
                    ),
                ),
            ],
        ),
    ]
