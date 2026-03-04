from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_adresse = models.CharField(max_length=255)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.client_name



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    contract_number = models.CharField(max_length=50, unique=True)

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="contracts"
    )

    products = models.ManyToManyField(
        Product,
        through="ContractProduct"
    )

    def __str__(self):
        return self.contract_number


class ContractProduct(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    factor = models.FloatField()
    amount_threshold = models.PositiveIntegerField()

    class Meta:
        unique_together = ("contract", "product")

    def __str__(self):
        return f"{ self.contract } - { self.product}"