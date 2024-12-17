from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    pin = models.CharField(max_length=4, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} (PIN: {self.pin})"
