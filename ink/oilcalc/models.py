from django.db import models

# # Create your models here.
class OilStock(models.Model):
    date = models.DateField()
    oil_stock_value = models.FloatField()


class OilAccumulation(models.Model):
    date = models.DateField()
    oil_accumulated = models.FloatField()
    water_accumulated = models.FloatField()
    water_accumulated_upload = models.FloatField()


class OilDebit(models.Model):
    date = models.DateField()
    oil_debit = models.FloatField()
    water_debit = models.FloatField()
    liquid_debit = models.FloatField()
    water_throttle_response = models.FloatField()
