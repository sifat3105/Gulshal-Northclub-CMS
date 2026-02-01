from django.contrib import admin
from .models import ContactPageImage, Appointment
from project.admin_helpers import CMSSingletonAdmin, CMSNoAddAdmin, image_preview, text_excerpt


@admin.register(ContactPageImage)
class ContactPageImageAdmin(CMSSingletonAdmin):
    list_display = ("id", "image_preview")

    @admin.display(description="Background")
    def image_preview(self, obj):
        return image_preview(obj, "contact_baground", width=120, height=70)


@admin.register(Appointment)
class AppointmentAdmin(CMSNoAddAdmin):
    list_display = ("id", "full_name", "email", "message_preview", "created_at")
    search_fields = ("full_name", "email", "message")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    @admin.display(description="Message")
    def message_preview(self, obj):
        return text_excerpt(obj.message, length=90)
