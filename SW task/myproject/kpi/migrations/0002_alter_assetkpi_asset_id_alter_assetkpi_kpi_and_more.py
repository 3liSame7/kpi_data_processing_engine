# Generated by Django 4.1 on 2024-10-31 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kpi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assetkpi",
            name="asset_id",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="assetkpi",
            name="kpi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assets",
                to="kpi.kpi",
            ),
        ),
        migrations.AlterField(
            model_name="kpi",
            name="expression",
            field=models.TextField(max_length=200),
        ),
    ]
