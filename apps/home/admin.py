from django.contrib import admin
from .models import (
    Hero,
    ClubFacilitiesHead,
    Facilities,
    OurMomentsHead,
    OurMoments,
    AffiliatCollabHead,
    AffiliatCollab,
    ClubEventHead,
    ClubEvents,
)
from project.admin_helpers import CMSSingletonAdmin, CMSModelAdmin, image_preview, text_excerpt


@admin.register(Hero)
class HeroAdmin(CMSSingletonAdmin):
    list_display = ("id", "title", "hero_preview", "created_at", "updated_at")

    @admin.display(description="Hero Image")
    def hero_preview(self, obj):
        return image_preview(obj, "bg_image", width=120, height=70)


@admin.register(ClubFacilitiesHead)
class ClubFacilitiesHeadAdmin(CMSSingletonAdmin):
    list_display = ("id", "head_text", "created_at", "updated_at")


@admin.register(Facilities)
class FacilitiesAdmin(CMSModelAdmin):
    list_display = ("id", "title", "designation_preview", "image_preview", "created_at")
    search_fields = ("title", "designation")

    @admin.display(description="Designation")
    def designation_preview(self, obj):
        return text_excerpt(obj.designation, length=80)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=60, height=60)


@admin.register(OurMomentsHead)
class OurMomentsHeadAdmin(CMSSingletonAdmin):
    list_display = ("id", "head_text", "sub_head", "created_at", "updated_at")


@admin.register(OurMoments)
class OurMomentsAdmin(CMSModelAdmin):
    list_display = ("id", "our_moment", "image_preview", "created_at")
    list_select_related = ("our_moment",)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=60, height=60)


@admin.register(AffiliatCollabHead)
class AffiliatCollabHeadAdmin(CMSSingletonAdmin):
    list_display = ("id", "head_text", "sub_head", "created_at", "updated_at")


@admin.register(AffiliatCollab)
class AffiliatCollabAdmin(CMSModelAdmin):
    list_display = ("id", "logo_preview", "created_at")

    @admin.display(description="Logo")
    def logo_preview(self, obj):
        return image_preview(obj, "logo", width=60, height=60)


@admin.register(ClubEventHead)
class ClubEventHeadAdmin(CMSSingletonAdmin):
    list_display = ("id", "head_text", "created_at", "updated_at")


@admin.register(ClubEvents)
class ClubEventsAdmin(CMSModelAdmin):
    list_display = ("id", "event_name", "description_preview", "image_preview", "created_at")
    search_fields = ("event_name", "description")

    @admin.display(description="Description")
    def description_preview(self, obj):
        return text_excerpt(obj.description, length=90)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "images", width=60, height=60)
