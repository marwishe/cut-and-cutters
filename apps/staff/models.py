from apps.branches.models import Branch
from config import settings
from django.db import models

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
    avatar = models.ImageField(upload_to='masters/avatar')

    def __str__(self):
        return self.name