from django.db import models

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=30, default="Pending")

    def __str__(self):
        return self.customer_name
