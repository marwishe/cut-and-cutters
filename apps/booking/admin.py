from django.contrib import admin
from .models import Booking
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'master', 'branch', 'starts_at', 'status')
    list_filter = ('status', 'branch')
    date_hierarchy = 'starts_at'