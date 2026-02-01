from django.contrib import admin
from .models import (
    AboutHero,
    Topgallery,
    Bottomgallery,
    AboutForHeritage,
    President,
    PresidentSocialMediaLink,
    MemberType,
    BoardMember,
    DetailImage,
    SocialMediaLink,
)
from project.admin_helpers import CMSSingletonAdmin, CMSModelAdmin, image_preview, text_excerpt


@admin.register(AboutHero)
class AboutHeroAdmin(CMSSingletonAdmin):
    list_display = ("id", "hero_image_preview")

    @admin.display(description="Hero Image")
    def hero_image_preview(self, obj):
        return image_preview(obj, "hero_image", width=120, height=70)


@admin.register(Topgallery)
class TopgalleryAdmin(CMSModelAdmin):
    list_display = ("id", "title", "subtitle_preview", "top_image_preview")
    search_fields = ("title", "sub_title")

    @admin.display(description="Subtitle")
    def subtitle_preview(self, obj):
        return text_excerpt(obj.sub_title, length=80)

    @admin.display(description="Top Image")
    def top_image_preview(self, obj):
        return image_preview(obj, "top_image", width=90, height=60)


@admin.register(Bottomgallery)
class BottomgalleryAdmin(CMSModelAdmin):
    list_display = ("id", "title", "subtitle_preview", "bottom_image_preview")
    search_fields = ("title", "sub_title")

    @admin.display(description="Subtitle")
    def subtitle_preview(self, obj):
        return text_excerpt(obj.sub_title, length=80)

    @admin.display(description="Bottom Image")
    def bottom_image_preview(self, obj):
        return image_preview(obj, "bottom_image", width=90, height=60)


@admin.register(AboutForHeritage)
class AboutForHeritageAdmin(CMSSingletonAdmin):
    list_display = ("id", "title", "description_preview", "image_preview")
    search_fields = ("title", "descriptions")

    @admin.display(description="Description")
    def description_preview(self, obj):
        return text_excerpt(obj.descriptions, length=90)

    @admin.display(description="Image")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=90, height=60)


class PresidentSocialMediaInline(admin.TabularInline):
    model = PresidentSocialMediaLink
    extra = 0


@admin.register(President)
class PresidentAdmin(CMSSingletonAdmin):
    list_display = ("name", "designation", "email", "image_preview")
    search_fields = ("name", "designation", "email")
    inlines = [PresidentSocialMediaInline]

    @admin.display(description="Photo")
    def image_preview(self, obj):
        return image_preview(obj, "image", width=60, height=60)


@admin.register(MemberType)
class MemberTypeAdmin(CMSModelAdmin):
    list_display = ("id", "type_name")
    search_fields = ("type_name",)


class DetailImageInline(admin.TabularInline):
    model = DetailImage
    extra = 0
    fields = ("detail_image", "image_preview")
    readonly_fields = ("image_preview",)

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return image_preview(obj, "detail_image", width=60, height=60)


class BoardMemberSocialMediaInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 0


@admin.register(BoardMember)
class BoardMemberAdmin(CMSModelAdmin):
    list_display = ("id", "member_name", "designation", "member_type", "photo_preview")
    list_filter = ("member_type",)
    search_fields = ("member_name", "designation")
    list_select_related = ("member_type",)
    inlines = [DetailImageInline, BoardMemberSocialMediaInline]

    @admin.display(description="Photo")
    def photo_preview(self, obj):
        return image_preview(obj, "member_image", width=60, height=60)
