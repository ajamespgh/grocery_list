from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50)


class List(models.Model):
    list_name = models.CharField(max_length=100)


class List_Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    notes = models.CharField(max_length=255)
