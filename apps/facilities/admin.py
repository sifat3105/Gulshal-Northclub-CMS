from django.contrib import admin
from .models import (
    PlaceImage,
    PlaceHighlight,
    PlaceOffer,
    LoungesParty,
    salon,
    healthcare_gym,
    SwimmingPool,
    BilliardSmoking,
    Library,
    BeautyParlor,
    Laundry,
    CardRoom,
    BanquetHall,
)
from project.admin_helpers import CMSModelAdmin, image_preview


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


class PlaceHighlightInline(admin.TabularInline):
    model = PlaceHighlight
    extra = 0
    fields = ("title", "sub_title", "icon", "icon_preview")
    readonly_fields = ("icon_preview",)

    @admin.display(description="Preview")
    def icon_preview(self, obj):
        return image_preview(obj, "icon", width=40, height=40)


class PlaceOfferInline(admin.TabularInline):
    model = PlaceOffer
    extra = 0
    fields = ("name", "icon", "icon_preview")
    readonly_fields = ("icon_preview",)

    @admin.display(description="Preview")
    def icon_preview(self, obj):
        return image_preview(obj, "icon", width=40, height=40)


class BasePlaceAdmin(CMSModelAdmin):
    inlines = [PlaceImageInline, PlaceHighlightInline, PlaceOfferInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "place_type", "slug")
    search_fields = ("title", "description")
    ordering = ("title",)

    place_type = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.place_type:
            return qs.filter(place_type=self.place_type)
        return qs

    def save_model(self, request, obj, form, change):
        if self.place_type:
            obj.place_type = self.place_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if "place_type" in fields:
            fields.remove("place_type")
        return fields

    def has_add_permission(self, request):
        if not self.place_type:
            return super().has_add_permission(request)
        return not self.model.objects.filter(place_type=self.place_type).exists()


@admin.register(healthcare_gym)
class HealthcareGymAdmin(BasePlaceAdmin):
    place_type = "healthcare_gym"


@admin.register(salon)
class SalonAdmin(BasePlaceAdmin):
    place_type = "salon"


@admin.register(LoungesParty)
class LoungesPartyAdmin(BasePlaceAdmin):
    place_type = "lounges_party"


@admin.register(SwimmingPool)
class SwimmingPoolAdmin(BasePlaceAdmin):
    place_type = "swimming_pool"


@admin.register(BilliardSmoking)
class BilliardSmokingAdmin(BasePlaceAdmin):
    place_type = "billiard_smoking"


@admin.register(Library)
class LibraryAdmin(BasePlaceAdmin):
    place_type = "library"


@admin.register(BeautyParlor)
class BeautyParlorAdmin(BasePlaceAdmin):
    place_type = "beauty_parlor"


@admin.register(Laundry)
class LaundryAdmin(BasePlaceAdmin):
    place_type = "laundry"


@admin.register(CardRoom)
class CardRoomAdmin(BasePlaceAdmin):
    place_type = "card_room"


@admin.register(BanquetHall)
class BanquetHallAdmin(BasePlaceAdmin):
    place_type = "banquet_hall"
