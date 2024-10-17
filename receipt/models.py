# models.py
from django.db import models

class TransactionForm(models.Model):
    acc_details = models.CharField(max_length=255)
    cust_reference = models.CharField(max_length=255)
    trans_date = models.DateField()
    val_date = models.DateField()
    amount = models.CharField(max_length=100)
    cheque_number = models.CharField(max_length=50)
    trans_ref = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Transaction: {self.trans_ref}"
