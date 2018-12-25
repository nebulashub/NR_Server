from django.db import models
from django.db.models import Model


class EthNrTotalModel(Model):
    date = models.IntegerField()
    nr_value = models.CharField(max_length=255)

    class Meta:
        db_table = "eth_nr_total"
