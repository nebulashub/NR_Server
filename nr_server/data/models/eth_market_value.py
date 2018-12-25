from django.db import models
from django.db.models import Model


class EthMarketValueModel(Model):
    date = models.IntegerField()
    opening = models.FloatField()
    closing = models.FloatField()
    highest = models.FloatField()
    lowest = models.FloatField()
    amount = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    total_circulation = models.CharField(max_length=100)

    class Meta:
        db_table = "eth_market_value"
