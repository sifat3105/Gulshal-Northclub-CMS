from django.contrib import admin
from .models import FooterBrand, UsefulLink, SocialMedia, ContactInfo, FooterCopyright
from project.admin_helpers import CMSSingletonAdmin, CMSModelAdmin, image_preview


@admin.register(FooterBrand)
class FooterBrandAdmin(CMSSingletonAdmin):
    list_display = ("id", "short_text", "background_preview", "logo_preview")

    @admin.display(description="Background")
    def background_preview(self, obj):
        return image_preview(obj, "baground_image", width=80, height=60)

    @admin.display(description="Logo")
    def logo_preview(self, obj):
        return image_preview(obj, "logo", width=60, height=60)


@admin.register(ContactInfo)
class ContactInfoAdmin(CMSSingletonAdmin):
    list_display = ("address_line1", "office_phone")


@admin.register(FooterCopyright)
class FooterCopyrightAdmin(CMSSingletonAdmin):
    list_display = ("text",)


@admin.register(UsefulLink)
class UsefulLinkAdmin(CMSModelAdmin):
    list_display = ("title", "url")
    search_fields = ("title", "url")


@admin.register(SocialMedia)
class SocialMediaAdmin(CMSModelAdmin):
    list_display = ("name", "icon_preview", "url")
    search_fields = ("name", "url")

    @admin.display(description="Icon")
    def icon_preview(self, obj):
        return image_preview(obj, "icon", width=30, height=30)
