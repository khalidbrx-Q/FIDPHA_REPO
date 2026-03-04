from django.db import models

from .models import Client, Product, Contract  # import your main models

class Sells(models.Model):
    sell_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sell_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Sells'

    def __str__(self):
        return f"{self.client} sold {self.quantity} x {self.product}"