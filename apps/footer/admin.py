from django.contrib import admin
from .models import (
    FooterBrand,
    UsefulLink,
    SocialMedia,
    ContactInfo,
    FooterCopyright
)

# Register your models here.

class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only allow adding if no object exists
        count = self.model.objects.count()
        if count == 0:
            return True
        return False

# Register models with singleton behavior
@admin.register(FooterBrand)
class FooterBrandAdmin(SingletonModelAdmin):
    list_display = ('short_text',)

@admin.register(ContactInfo)
class ContactInfoAdmin(SingletonModelAdmin):
    list_display = ('address_line1', 'office_phone')

@admin.register(FooterCopyright)
class FooterCopyrightAdmin(SingletonModelAdmin):
    list_display = ('text',)

# Useful links & social media can have multiple entries
@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'url')
