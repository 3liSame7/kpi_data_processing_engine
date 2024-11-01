# Generated by Django 4.1 on 2024-10-31 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kpi", "0002_alter_assetkpi_asset_id_alter_assetkpi_kpi_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetkpi",
            name="asset_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="assetkpi",
            name="kpi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="kpi.kpi"
            ),
        ),
        migrations.AlterField(
            model_name="kpi",
            name="expression",
            field=models.TextField(),
        ),
    ]
