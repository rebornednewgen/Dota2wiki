from django.db import models
from django.contrib.auth.models import User


class Hero(models.Model):
    ATTRIBUTE_CHOICES = [
        ('STR', 'Сила'),
        ('AGI', 'Ловкость'),
        ('INT', 'Интеллект'),
    ]

    ROLE_CHOICES = [
        ('CARRY', 'Керри'),
        ('SUPPORT', 'Саппорт'),
        ('MID', 'Мидлейнер'),
        ('OFFLANE', 'Оффлейнер'),
    ]

    name = models.CharField("Имя героя", max_length=100)
    attribute = models.CharField("Атрибут", max_length=3, choices=ATTRIBUTE_CHOICES)
    role = models.CharField("Роль", max_length=10, choices=ROLE_CHOICES)
    lore = models.TextField("История")
    image = models.ImageField("Изображение", upload_to='heroes/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.name