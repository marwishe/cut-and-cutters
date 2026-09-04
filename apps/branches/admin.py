from django.contrib import admin
from .models import Branch
# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'is_active')
    list_filter = ('is_active',)