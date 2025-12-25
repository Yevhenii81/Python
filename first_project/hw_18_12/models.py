from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    year = models.IntegerField()
    style = models.CharField(max_length=100)
    publisher = models.CharField(max_length=150)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    register_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
