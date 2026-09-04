from django.contrib import admin
from .models import Booking
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'master', 'branch', 'starts_at', 'status')
    list_filter = ('status', 'master__branch')
    date_hierarchy = 'starts_at'

    def branch(self, obj):
        return obj.master.branch
    branch.short_description='Филиал'
    branch.admin_order_field='master__branch'