from django.utils.text import slugify
from django.db.models import CASCADE
from django.db.models import IntegerChoices
from apps.branches.models import Branch
from config import settings
from django.db import models


def master_avatar_path(instance, filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return f'masters/{instance.slug}/avatar.{ext}'

# Create your models here.
class Master(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='master_profile'
    )

    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name='masters')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    avatar = models.ImageField(upload_to=master_avatar_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Master.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class WorkingHours(models.Model):
    class Weekday(IntegerChoices):
        MONDAY = 0, 'Понедельник'
        TUESDAY = 1, 'Вторник'
        WEDNESDAY = 2, 'Среда'
        THURSDAY = 3, 'Четверг'
        FRIDAY = 4, 'Пятница'
        SATURDAY = 5, 'Суббота'
        SUNDAY = 6, 'Воскресенье'

    master = models.ForeignKey(Master, on_delete=CASCADE, related_name='working_hours')
    weekday = models.IntegerField(choices=Weekday.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_day_off = models.BooleanField(default=False)

    class Meta:
        ordering=['master', 'weekday']
        unique_together=['master', 'weekday']
        verbose_name='Рабочие часы'
        verbose_name_plural='Рабочие часы'

    def __str__(self):
        return f'{self.master.name} – {self.get_weekday_display()}'