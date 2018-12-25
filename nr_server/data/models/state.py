from django.db import models
from django.db.models import Model


class StateModel(Model):
    key = models.CharField(max_length=50)
    value = models.TextField()

    class Meta:
        db_table = "state"
