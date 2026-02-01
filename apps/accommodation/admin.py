from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions
)

# ONE-TIME DATA MODELS
class SingleObjectAdmin(admin.ModelAdmin):
    """Allow only 1 object. After creation, redirect to edit page."""

    def has_add_permission(self, request):
        # Allow add only if no object exists 
        if self.model.objects.count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    def changelist_view(self, request, extra_context=None):
        # Redirect list page to existing object's edit page
        obj = self.model.objects.first()
        if obj:
            return redirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                        args=[obj.pk])
            )
        else:
            return redirect(
                reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_add")
            )


# Accommodation Hero Admin
@admin.register(AccommodationHero)
class AccommodationHeroAdmin(SingleObjectAdmin):
    list_display = ('id', 'title', 'sub_title', 'created_at', 'updated_at')
    search_fields = ('title', )


# Gallery Image Admin
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title', )


# Banner Image Admin
@admin.register(BannerImage)
class BannerImageAdmin(SingleObjectAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title', )


# Luxury Admin
@admin.register(Luxury)
class LuxuryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title', )


# Provide (We Provide Section) Admin
@admin.register(Provide)
class ProvideAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'created_at', 'updated_at')
    search_fields = ('service_name', )


# Below Impressions Admin
@admin.register(ImpressionsImages)
class ImpressionsImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')


# Impressions Admin
@admin.register(Impressions)
class ImpressionsAdmin(SingleObjectAdmin):
    list_display = ('id', 'title','created_at', 'updated_at')
    search_fields = ('title', )
