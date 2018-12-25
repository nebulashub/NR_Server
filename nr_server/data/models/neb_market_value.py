from django.db import models
from django.db.models import Model


class NebMarketValueModel(Model):
    date = models.IntegerField()
    opening = models.FloatField()
    closing = models.FloatField()
    highest = models.FloatField()
    lowest = models.FloatField()
    amount = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    total_circulation = models.CharField(max_length=100)

    class Meta:
        db_table = "neb_market_value"
