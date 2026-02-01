from django.contrib import admin
from .models import (
    PlaceImage, PlaceHighlight, PlaceOffer,LoungesParty,salon,
    healthcare_gym,SwimmingPool, BilliardSmoking, Library,
    BeautyParlor, Laundry, CardRoom, BanquetHall
)

# Register your models here.


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1


class PlaceHighlightInline(admin.TabularInline):
    model = PlaceHighlight
    extra = 1


class PlaceOfferInline(admin.TabularInline):
    model = PlaceOffer
    extra = 1


class BasePlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline, PlaceHighlightInline, PlaceOfferInline]
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "place_type")


def save_with_type(type_name):
    def save_model(self, request, obj, form, change):
        obj.place_type = type_name
        super(self.__class__, self).save_model(request, obj, form, change)
    return save_model


@admin.register(healthcare_gym)
class healthcare_gymAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="healthcare_gym")
    save_model = save_with_type("healthcare_gym")

@admin.register(salon)
class salonAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="salon")
    save_model = save_with_type("salon")

@admin.register(LoungesParty)
class LoungesPartyAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="lounges_party")
    save_model = save_with_type("lounges_party")

@admin.register(SwimmingPool)
class SwimmingPoolAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="swimming_pool")
    save_model = save_with_type("swimming_pool")


@admin.register(BilliardSmoking)
class BilliardSmokingAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="billiard_smoking")
    save_model = save_with_type("billiard_smoking")


@admin.register(Library)
class LibraryAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="library")
    save_model = save_with_type("library")


@admin.register(BeautyParlor)
class BeautyParlorAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="beauty_parlor")
    save_model = save_with_type("beauty_parlor")


@admin.register(Laundry)
class LaundryAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="laundry")
    save_model = save_with_type("laundry")


@admin.register(CardRoom)
class CardRoomAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="card_room")
    save_model = save_with_type("card_room")


@admin.register(BanquetHall)
class BanquetHallAdmin(BasePlaceAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(place_type="banquet_hall")
    save_model = save_with_type("banquet_hall")
