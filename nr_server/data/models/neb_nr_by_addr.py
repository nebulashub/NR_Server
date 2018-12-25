from django.db import models
from django.db.models import Model


class NebNrByAddrModel(Model):
    address = models.CharField(max_length=35)
    data = models.BinaryField()
    last_above_0_dates = models.CharField(max_length=255)
    last_above_0_num = models.IntegerField()

    class Meta:
        db_table = "neb_nr_by_addr"
