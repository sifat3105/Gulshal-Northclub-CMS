from django.contrib import admin
from .models import (
    Gallery,
    GalleryImage,
    MembershipGallery,
    ReservationGallery,
    MenuGallery,GallerySection,
    GallerySectionImage,
    # ======================================
    MembershipFineDining,MembershipLiveMusic,MembershipFineDiningSecond,
    ReservationFineDining,ReservationLiveMusic,ReservationFineDiningSecond,
    MenuFineDining,MenuLiveMusic,MenuFineDiningSecond
)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class BaseGalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ("gallery_type", "is_active", "created_at")
    ordering = ("-id",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(self, "gallery_type"):
            return qs.filter(gallery_type=self.gallery_type)
        return qs

    def save_model(self, request, obj, form, change):
        if hasattr(self, "gallery_type"):
            obj.gallery_type = self.gallery_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if "gallery_type" in fields:
            fields.remove("gallery_type")
        return fields

@admin.register(MembershipGallery)
class MembershipGalleryAdmin(BaseGalleryAdmin):
    gallery_type = "memberships"

@admin.register(ReservationGallery)
class ReservationGalleryAdmin(BaseGalleryAdmin):
    gallery_type = "reservation"

@admin.register(MenuGallery)
class MenuGalleryAdmin(BaseGalleryAdmin):
    gallery_type = "menu"



# ==============
class GallerySectionImageInline(admin.TabularInline):
    model = GallerySectionImage
    extra = 1

class BaseGalleryAdmin(admin.ModelAdmin):
    inlines = [GallerySectionImageInline]
    list_display = ("page", "section_type", "is_active")

    page = None
    section_type = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(page=self.page, section_type=self.section_type)

    def save_model(self, request, obj, form, change):
        obj.page = self.page
        obj.section_type = self.section_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        for f in ("page", "section_type"):
            if f in fields:
                fields.remove(f)
        return fields


# ===== MEMBERSHIPS =====
@admin.register(MembershipFineDining)
class MFDA(BaseGalleryAdmin):
    page = "memberships"
    section_type = "fine_dining"


@admin.register(MembershipLiveMusic)
class MLMA(BaseGalleryAdmin):
    page = "memberships"
    section_type = "live_music"


@admin.register(MembershipFineDiningSecond)
class MFDSA(BaseGalleryAdmin):
    page = "memberships"
    section_type = "fine_dining_2"


# ===== RESERVATION =====
@admin.register(ReservationFineDining)
class RFDA(BaseGalleryAdmin):
    page = "reservation"
    section_type = "fine_dining"


@admin.register(ReservationLiveMusic)
class RLMA(BaseGalleryAdmin):
    page = "reservation"
    section_type = "live_music"


@admin.register(ReservationFineDiningSecond)
class RFDSA(BaseGalleryAdmin):
    page = "reservation"
    section_type = "fine_dining_2"


# ===== MENU =====
@admin.register(MenuFineDining)
class MFDA2(BaseGalleryAdmin):
    page = "menu"
    section_type = "fine_dining"


@admin.register(MenuLiveMusic)
class MLMA2(BaseGalleryAdmin):
    page = "menu"
    section_type = "live_music"


@admin.register(MenuFineDiningSecond)
class MFDSA2(BaseGalleryAdmin):
    page = "menu"
    section_type = "fine_dining_2"
