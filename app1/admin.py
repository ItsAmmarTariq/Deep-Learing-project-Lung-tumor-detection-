# app1/admin.py

from django.contrib import admin
from .models import Medicine,Doctor

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name')