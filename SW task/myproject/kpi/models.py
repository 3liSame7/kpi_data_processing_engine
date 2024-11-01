from django.db import models

class KPI(models.Model):
    name = models.CharField(max_length=100)
    expression = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class AssetKPI(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    asset_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.kpi.name} - Asset {self.asset_id}"

