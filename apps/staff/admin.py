from django.contrib import admin
from .models import Master, WorkingHours

# Register your models here.
class WorkingHoursInline(admin.TabularInline):
    model = WorkingHours
    extra = 1

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'user')
    list_filter = ('branch',)
    inlines = [WorkingHoursInline]
    prepopulated_fields = {'slug': ('name',)}