from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin


# SINGLE OBJECT ADMIN
class SingleObjectAdmin(ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.count() < 1

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = self.model.objects.first()
        if obj:
            return redirect(reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                args=[obj.id]
            ))
        else:
            return redirect(reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_add"
            ))


# HERO
@admin.register(Hero)
class HeroAdmin(SingleObjectAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')


# CLUB FACILITIES HEAD
@admin.register(ClubFacilitiesHead)
class ClubFacilitiesHeadAdmin(SingleObjectAdmin):
    list_display = ('id', 'head_text', 'created_at', 'updated_at')


# FACILITIES
@admin.register(Facilities)
class FacilitiesAdmin(ModelAdmin):
    list_display = ('id', 'title', 'designation', 'created_at', 'updated_at')


# OUR MOMENTS HEAD
@admin.register(OurMomentsHead)
class OurMomentsHeadAdmin(SingleObjectAdmin):
    list_display = ('id', 'head_text', 'sub_head', 'created_at', 'updated_at')


# OUR MOMENTS
@admin.register(OurMoments)
class OurMomentsAdmin(ModelAdmin):
    list_display = ('id', 'our_moment', 'created_at', 'updated_at')


# AFFILIATION HEAD
@admin.register(AffiliatCollabHead)
class AffiliatCollabHeadAdmin(SingleObjectAdmin):
    list_display = ('id', 'head_text', 'sub_head', 'created_at', 'updated_at')


# AFFILIATIONS LOGO
@admin.register(AffiliatCollab)
class AffiliatCollabAdmin(ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')


# CLUB EVENT HEAD
@admin.register(ClubEventHead)
class ClubEventHeadAdmin(SingleObjectAdmin):
    list_display = ('id', 'head_text', 'created_at', 'updated_at')


# CLUB EVENTS
@admin.register(ClubEvents)
class ClubEventsAdmin(ModelAdmin):
    list_display = ('id', 'event_name', 'created_at', 'updated_at')
