from django.db import models
from django.db.models import Model


class NebNrTotalModel(Model):
    date = models.IntegerField()
    nr_value = models.CharField(max_length=255)

    class Meta:
        db_table = "neb_nr_total"
