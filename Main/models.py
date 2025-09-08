from django.db import models

class Member(models.Model):
    FullName = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,unique=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.FullName} ({self.pk})"
