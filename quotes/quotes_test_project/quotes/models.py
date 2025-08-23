from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Qoute(models.Model):
    """Модель цитаты."""

    source = models.ForeignKey(
        Source, on_delete=models.CASCADE,
        verbose_name="Источник цитаты.",
        related_name="Цитаты"
    )
    quote_text = models.TextField(verbose_name="Текст цитаты")
    weight = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], 
        verbose_name="Вес"
    )
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    likes = models.PositiveIntegerField(
        default=0, verbose_name="Количество лайков"
    )
    dislikes = models.PositiveIntegerField(
        default=0, verbose_name="Количество дизлайков"
    )

    class Meta:
        unique_together = ['source', 'quote_text']
