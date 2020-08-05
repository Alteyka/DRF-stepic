from django.db import models


class ProductSets(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Recipient(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.surname


class Order(models.Model):
    CREATED = 'created'
    DELIVERED = 'delivered'
    PROCESSED = 'processed'
    CANCELLED = 'cancelled'
    PROCESS_CHOICES = [
        (CREATED, 'created'),
        (DELIVERED, 'delivered'),
        (PROCESSED, 'processed'),
        (CANCELLED, 'cancelled')
    ]
    order_created_datetime = models.DateTimeField()
    delivery_datetime = models.DateTimeField()
    delivery_address = models.CharField(max_length=200)
    recipient = models.ForeignKey('Recipient', on_delete=models.CASCADE)
    product_set = models.ForeignKey('ProductSets', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=PROCESS_CHOICES)

    def __str__(self):
        return str(self.recipient)
