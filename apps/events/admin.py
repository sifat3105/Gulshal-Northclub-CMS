from django.contrib import admin
from .models import (
    RunningEventHero,
    UpcomingEventHero,
    PastEventHero,
    EventImage,
    RunningEvent,
    UpcomingEvent,
    PastEventPhoto,
    PastEvent,
    CompletedEvent,
    FineDining,
    LiveMusic,
    FineDiningSecond,
    EventGallery,
)
from project.admin_helpers import CMSModelAdmin, image_preview


class BaseEventHeroAdmin(CMSModelAdmin):
    list_display = ("hero_title", "hero_preview", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("hero_title", "hero_description")
    ordering = ("-id",)

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

    def has_add_permission(self, request):
        return not self.model.objects.filter(event_type=self.event_type).exists()

    @admin.display(description="Image")
    def hero_preview(self, obj):
        return image_preview(obj, "hero_image", width=120, height=70)


@admin.register(RunningEventHero)
class RunningEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "running"


@admin.register(UpcomingEventHero)
class UpcomingEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "upcoming"


@admin.register(PastEventHero)
class PastEventHeroAdmin(BaseEventHeroAdmin):
    event_type = "past"


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=80, height=60)


class BaseEventAdmin(CMSModelAdmin):
    inlines = [EventImageInline]
    list_display = ("title", "event_date", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    date_hierarchy = "event_date"
    ordering = ("-event_date", "-id")

    event_type = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.event_type:
            return qs.filter(event_type=self.event_type)
        return qs

    def save_model(self, request, obj, form, change):
        if self.event_type:
            obj.event_type = self.event_type
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if "event_type" in fields:
            fields.remove("event_type")
        return fields


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


@admin.register(FineDining)
class FineDiningAdmin(BaseEventAdmin):
    event_type = "fine_dining"


@admin.register(LiveMusic)
class LiveMusicAdmin(BaseEventAdmin):
    event_type = "live_music"


@admin.register(FineDiningSecond)
class FineDiningSecondAdmin(BaseEventAdmin):
    event_type = "fine_dining_2"


@admin.register(EventGallery)
class EventGalleryAdmin(BaseEventAdmin):
    event_type = "gallery"
