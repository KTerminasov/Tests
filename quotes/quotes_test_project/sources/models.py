from django.db import models


class Source(models.Model):
    """Модель источника цитаты."""

    TAG_CHOICES = [
        ('Book', 'Книга'),
        ('Movie', 'Фильм'),
        ('Series', 'Сериал'),
        ('Game', 'Игра'),
        ('Scientific article', 'Научная статья'),
        ('Other', 'Другое'),
    ]

    title = models.CharField(max_length=100, verbose_name="Название источника")
    tag = models.CharField(
        max_length=20, choices=TAG_CHOICES, verbose_name="Тег"
    )

    class Meta:
        unique_together = ['title', 'tag']

    def __str__(self):
        return self.title
