from django.contrib import admin
from .models import ContactPageImage, Appointment

# Register your models here.

@admin.register(ContactPageImage)
class ContactPageImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_baground')  
    readonly_fields = ('contact_baground',)   
    search_fields = ('contact_baground',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

