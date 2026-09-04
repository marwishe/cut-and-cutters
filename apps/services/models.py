from apps.staff.models import Master
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    masters = models.ManyToManyField(
        Master,
        related_name='services',
        blank=True
    )

    class Meta:
        ordering=['name']
        verbose_name='Услуга'
        verbose_name_plural='Услуги'

    def __str__(self):
        return self.name