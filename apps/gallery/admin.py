from django.contrib import admin
from .models import (
    GalleryImage,
    MembershipGallery,
    ReservationGallery,
    MenuGallery,
    GallerySectionImage,
    MembershipFineDining,
    MembershipLiveMusic,
    MembershipFineDiningSecond,
    ReservationFineDining,
    ReservationLiveMusic,
    ReservationFineDiningSecond,
    MenuFineDining,
    MenuLiveMusic,
    MenuFineDiningSecond,
)
from project.admin_helpers import CMSModelAdmin, image_preview


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


class BaseGalleryTypeAdmin(CMSModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ("title", "gallery_type", "is_active", "created_at")
    list_filter = ("is_active",)
    ordering = ("-id",)

    gallery_type = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.gallery_type:
            return qs.filter(gallery_type=self.gallery_type)
        return qs

    def save_model(self, request, obj, form, change):
        if self.gallery_type:
            obj.gallery_type = self.gallery_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if "gallery_type" in fields:
            fields.remove("gallery_type")
        return fields

    def has_add_permission(self, request):
        if not self.gallery_type:
            return super().has_add_permission(request)
        return not self.model.objects.filter(gallery_type=self.gallery_type).exists()


@admin.register(MembershipGallery)
class MembershipGalleryAdmin(BaseGalleryTypeAdmin):
    gallery_type = "memberships"


@admin.register(ReservationGallery)
class ReservationGalleryAdmin(BaseGalleryTypeAdmin):
    gallery_type = "reservation"


@admin.register(MenuGallery)
class MenuGalleryAdmin(BaseGalleryTypeAdmin):
    gallery_type = "menu"


class GallerySectionImageInline(admin.TabularInline):
    model = GallerySectionImage
    extra = 0
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


class BaseGallerySectionAdmin(CMSModelAdmin):
    inlines = [GallerySectionImageInline]
    list_display = ("title", "page", "section_type", "is_active", "created_at")
    list_filter = ("is_active",)
    ordering = ("-id",)

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
        fields = list(super().get_fields(request, obj))
        for field_name in ("page", "section_type"):
            if field_name in fields:
                fields.remove(field_name)
        return fields

    def has_add_permission(self, request):
        return not self.model.objects.filter(
            page=self.page, section_type=self.section_type
        ).exists()


@admin.register(MembershipFineDining)
class MembershipFineDiningAdmin(BaseGallerySectionAdmin):
    page = "memberships"
    section_type = "fine_dining"


@admin.register(MembershipLiveMusic)
class MembershipLiveMusicAdmin(BaseGallerySectionAdmin):
    page = "memberships"
    section_type = "live_music"


@admin.register(MembershipFineDiningSecond)
class MembershipFineDiningSecondAdmin(BaseGallerySectionAdmin):
    page = "memberships"
    section_type = "fine_dining_2"


@admin.register(ReservationFineDining)
class ReservationFineDiningAdmin(BaseGallerySectionAdmin):
    page = "reservation"
    section_type = "fine_dining"


@admin.register(ReservationLiveMusic)
class ReservationLiveMusicAdmin(BaseGallerySectionAdmin):
    page = "reservation"
    section_type = "live_music"


@admin.register(ReservationFineDiningSecond)
class ReservationFineDiningSecondAdmin(BaseGallerySectionAdmin):
    page = "reservation"
    section_type = "fine_dining_2"


@admin.register(MenuFineDining)
class MenuFineDiningAdmin(BaseGallerySectionAdmin):
    page = "menu"
    section_type = "fine_dining"


@admin.register(MenuLiveMusic)
class MenuLiveMusicAdmin(BaseGallerySectionAdmin):
    page = "menu"
    section_type = "live_music"


@admin.register(MenuFineDiningSecond)
class MenuFineDiningSecondAdmin(BaseGallerySectionAdmin):
    page = "menu"
    section_type = "fine_dining_2"
