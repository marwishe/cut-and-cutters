from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    # добавить longtitude & latitude для карты в будущем

    class Meta:
        ordering = ['name']
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name