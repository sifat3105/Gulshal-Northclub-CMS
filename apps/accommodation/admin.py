from django.contrib import admin
from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions,
)
from project.admin_helpers import CMSSingletonAdmin, CMSModelAdmin, image_preview, text_excerpt


@admin.register(AccommodationHero)
class AccommodationHeroAdmin(CMSSingletonAdmin):
    list_display = ("id", "title", "hero_preview", "created_at", "updated_at")
    search_fields = ("title",)

    @admin.display(description="Hero Image")
    def hero_preview(self, obj):
        return image_preview(obj, "bg_image", width=120, height=70)


@admin.register(GalleryImage)
class GalleryImageAdmin(CMSModelAdmin):
    list_display = ("id", "title", "top_image_preview", "below_image_preview", "created_at")
    search_fields = ("title",)

    @admin.display(description="Top Image")
    def top_image_preview(self, obj):
        return image_preview(obj, "top_image", width=80, height=60)

    @admin.display(description="Below Image")
    def below_image_preview(self, obj):
        return image_preview(obj, "below_image", width=80, height=60)


@admin.register(BannerImage)
class BannerImageAdmin(CMSSingletonAdmin):
    list_display = ("id", "title", "banner_preview", "created_at", "updated_at")
    search_fields = ("title",)

    @admin.display(description="Banner")
    def banner_preview(self, obj):
        return image_preview(obj, "banner_image", width=120, height=70)


@admin.register(Luxury)
class LuxuryAdmin(CMSModelAdmin):
    list_display = ("id", "title", "image_preview", "created_at")
    search_fields = ("title",)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


@admin.register(Provide)
class ProvideAdmin(CMSModelAdmin):
    list_display = ("id", "service_name", "icon_preview", "description_preview", "created_at")
    search_fields = ("service_name", "short_descriptions")

    @admin.display(description="Icon")
    def icon_preview(self, obj):
        return image_preview(obj, "service_icon", width=40, height=40)

    @admin.display(description="Description")
    def description_preview(self, obj):
        return text_excerpt(obj.short_descriptions, length=80)


class ImpressionsImagesInline(admin.TabularInline):
    model = ImpressionsImages
    extra = 0
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


@admin.register(Impressions)
class ImpressionsAdmin(CMSSingletonAdmin):
    list_display = ("id", "title", "logo_preview", "created_at", "updated_at")
    search_fields = ("title",)
    inlines = [ImpressionsImagesInline]

    @admin.display(description="Logo")
    def logo_preview(self, obj):
        return image_preview(obj, "logo", width=60, height=60)


@admin.register(ImpressionsImages)
class ImpressionsImagesAdmin(CMSModelAdmin):
    list_display = ("id", "impression", "image_preview", "created_at")
    list_select_related = ("impression",)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)
