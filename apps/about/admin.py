from django.contrib import admin
from django.utils.html import mark_safe
from .models import *
# About Section
@admin.register(AboutHero)
class AboutHeroAdmin(admin.ModelAdmin):
    list_display = ("id", "hero_image_preview")
    
    def hero_image_preview(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" width="100" height="60" style="object-fit:cover;border-radius:5px;" />')
        return "No Image"
    hero_image_preview.short_description = "Hero Image Preview"


@admin.register(Topgallery)
class TopgalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sub_title", "top_image_preview")
    search_fields = ("title", "sub_title")
    
    def top_image_preview(self, obj):
        if obj.top_image:
            return mark_safe(f'<img src="{obj.top_image.url}" width="80" height="50" style="object-fit:cover;border-radius:5px;" />')
        return "No Image"
    top_image_preview.short_description = "Top Image Preview"


@admin.register(Bottomgallery)
class BottomgalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sub_title", "bottom_image_preview")
    search_fields = ("title", "sub_title")
    
    def bottom_image_preview(self, obj):
        if obj.bottom_image:
            return mark_safe(f'<img src="{obj.bottom_image.url}" width="80" height="50" style="object-fit:cover;border-radius:5px;" />')
        return "No Image"
    bottom_image_preview.short_description = "Bottom Image Preview"


@admin.register(AboutForHeritage)
class AboutForHeritageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "descriptions", "heritage_image_preview")
    search_fields = ("title", "descriptions")
    
    def heritage_image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" height="50" style="object-fit:cover;border-radius:5px;" />')
        return "No Image"
    heritage_image_preview.short_description = "Image Preview"


# Member Section
class SocialMediaLinkInline(admin.TabularInline):
    model = PresidentSocialMediaLink
    extra = 1


@admin.register(President)
class PresidentAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email')
    search_fields = ('name', 'designation', 'email')
    inlines = [SocialMediaLinkInline]


@admin.register(MemberType)
class MemberTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")
    search_fields = ("type_name",)


class DetailImageInline(admin.TabularInline):
    model = DetailImage
    extra = 1


class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "member_name", "designation", "member_type", "image_preview")
    list_filter = ("member_type",)
    search_fields = ("member_name", "designation")
    inlines = [DetailImageInline, SocialMediaLinkInline]

    def image_preview(self, obj):
        if obj.member_image:
            return mark_safe(f'<img src="{obj.member_image.url}" width="60" height="60" style="object-fit:cover;border-radius:5px;" />')
        return "No Image"
    image_preview.short_description = "Preview"
