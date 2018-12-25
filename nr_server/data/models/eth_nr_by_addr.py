from django.db import models
from django.db.models import Model


class EthNrByAddrModel(Model):
    address = models.CharField(max_length=42)
    data = models.BinaryField()
    last_above_0_dates = models.CharField(max_length=255)
    last_above_0_num = models.IntegerField()

    class Meta:
        db_table = "eth_nr_by_addr"
