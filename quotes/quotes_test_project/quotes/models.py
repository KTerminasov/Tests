from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from sources.models import Source


class Quote(models.Model):
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
