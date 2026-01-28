from django.contrib import admin
from .models import Service, Order

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')

