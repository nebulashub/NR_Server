from django.db import models
from django.db.models import Model


class EthNrByDateModel(Model):
    date = models.IntegerField()
    data = models.BinaryField()

    class Meta:
        db_table = "eth_nr_by_date"
