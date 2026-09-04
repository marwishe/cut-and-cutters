from django.core.exceptions import ValidationError
from apps.staff.models import Master
from apps.services.models import Service
from apps.branches.models import Branch
from django.db import models

# Create your models here.
class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает подтверждения',
        CONFIRMED = 'confirmed', 'Подтверждена',
        CANCELLED = 'cancelled', 'Отменена'
        COMPLETED = 'completed', 'Завершена'

    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)

    #branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='bookings')
    master = models.ForeignKey(Master, on_delete=models.PROTECT, related_name='bookings')

    starts_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-starts_at']
        verbose_name='Запись'
        verbose_name_plural='Записи'

    def __str__(self):
        return f'{self.client_name} – {self.service.name} у {self.master.name} ({self.starts_at:%d.%m %H:%M})'
    
    def clean(self):
        super().clean()
        if self.master_id and self.service_id:
            if not self.service.masters.filter(pk=self.master_id).exists():
                raise ValidationError({
                    'master': f'«{self.master}» не выполняет услугу «{self.service}».'
                })
