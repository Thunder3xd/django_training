from django.db import models


# Create your models here.

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="nume")
    order_phone = models.CharField(max_length=200, verbose_name="numar")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Comanda"
        verbose_name_plural = "comenzi"
