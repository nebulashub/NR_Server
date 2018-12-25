from django.db import models
from django.db.models import Model


class NebNrByDateModel(Model):
    date = models.IntegerField()
    data = models.BinaryField()

    class Meta:
        db_table = "neb_nr_by_date"
