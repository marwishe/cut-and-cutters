from datetime import timedelta
from django.utils import timezone
from django.db import models

# Create your models here.
class PhoneVerification(models.Model):
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name='Верификация телефона'
        verbose_name_plural='Верификации телефонов'

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at

    def __str__(self):
        status = 'использован' if self.is_used else ('истёк' if self.is_expired() else 'активен')
        return f'{self.phone} ({status})'