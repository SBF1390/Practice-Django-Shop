from django.db import models


class Products(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Is_Available = models.BooleanField()

    def __str__(self):
        return f"{self.Name} ({self.pk})"


class Member(models.Model):
    FullName = models.CharField(max_length=100)
    Username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.FullName} ({self.pk})"


class Cart(models.Model):
    Products = models.ManyToManyField(Products)
    Total_price = models.IntegerField()
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    Quantity = models.IntegerField(default=1)
    Date = models.DateField(auto_now=True)
    Finished = models.BooleanField(default=False)
