from django.db import models

# ===== Задание 1 — Предсказания =====
class FortuneCookie(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


# ===== Задание 3 — Вирши (стихи) =====
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Poem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='poems')
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, related_name='poems')
    text = models.TextField()

    def __str__(self):
        return self.title
