from django.contrib import admin
from .models import (
    # event hero section
    EventHero, RunningEventHero, 
    UpcomingEventHero, PastEventHero,
    # event section
    Event,EventImage,RunningEvent,UpcomingEvent,PastEventPhoto,
    PastEvent,CompletedEvent,FineDining,
    LiveMusic,FineDiningSecond,EventGallery,
)

# Event hero admin
class BaseEventHeroAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "is_active")
    list_filter = ("is_active",)

    event_type = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(event_type=self.event_type)

    def save_model(self, request, obj, form, change):
        obj.event_type = self.event_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if "event_type" in fields:
            fields.remove("event_type")
        return fields


@admin.register(RunningEventHero)
class RunningEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "running"


@admin.register(UpcomingEventHero)
class UpcomingEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "upcoming"


@admin.register(PastEventHero)
class PastEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "past"




# Event section admin
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class BaseEventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    list_display = ("title", "event_type", "event_date")
    ordering = ("-id",)

    # 🔹 Filter per proxy (IMPORTANT)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(self, "event_type"):
            return qs.filter(event_type=self.event_type)
        return qs

    # 🔹 Auto set event_type on save
    def save_model(self, request, obj, form, change):
        if hasattr(self, "event_type"):
            obj.event_type = self.event_type
        super().save_model(request, obj, form, change)

    # 🔹 Hide event_type field from form (NO CONFUSION)
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if "event_type" in fields:
            fields.remove("event_type")
        return fields


# ===== EVENT STATUS =====
@admin.register(RunningEvent)
class RunningEventAdmin(BaseEventAdmin):
    event_type = "running"


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(BaseEventAdmin):
    event_type = "upcoming"


@admin.register(PastEvent)
class PastEventAdmin(BaseEventAdmin):
    event_type = "past"

@admin.register(PastEventPhoto)
class PastEventPhotoAdmin(BaseEventAdmin):
    event_type = "past_photo"

@admin.register(CompletedEvent)
class CompletedEventAdmin(BaseEventAdmin):
    event_type = "completed"


# ===== EXPERIENCE SECTIONS =====
@admin.register(FineDining)
class FineDiningAdmin(BaseEventAdmin):
    event_type = "fine_dining"


@admin.register(LiveMusic)
class LiveMusicAdmin(BaseEventAdmin):
    event_type = "live_music"


@admin.register(FineDiningSecond)
class FineDiningSecondAdmin(BaseEventAdmin):
    event_type = "fine_dining_2"


# ===== GALLERY =====
@admin.register(EventGallery)
class EventGalleryAdmin(BaseEventAdmin):
    event_type = "gallery"
