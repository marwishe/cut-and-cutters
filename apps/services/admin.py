from django.contrib import admin
from .models import Service
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'is_active')
    list_filter = ('is_active',)
    filter_horizontal = ('masters',)