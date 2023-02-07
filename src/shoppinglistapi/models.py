from django.db import models

class ShoppingListDB(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)

class ShoppingListDetailDB(models.Model):
    user_name = models.ForeignKey(ShoppingListDB, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField()


