from django.db import models

class Restaurant(models.Model):
    name = models.CharField("Назва", max_length=200)
    specialty = models.CharField("Спеціалізація", max_length=100)
    address = models.CharField("Адреса", max_length=300)
    website = models.URLField("Вебсайт", blank=True)
    phone = models.CharField("Контактний телефон", max_length=20)

    def __str__(self):
        return f"{self.name} ({self.specialty})"
