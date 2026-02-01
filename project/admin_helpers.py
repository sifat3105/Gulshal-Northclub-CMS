from django.contrib import admin
from django.utils.html import format_html

try:
    from unfold.admin import ModelAdmin as BaseModelAdmin
except Exception:  # pragma: no cover - fallback if unfold is unavailable
    BaseModelAdmin = admin.ModelAdmin


class CMSModelAdmin(BaseModelAdmin):
    list_per_page = 25
    save_on_top = True

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        field_names = {field.name for field in self.model._meta.fields}
        for field_name in ("created_at", "updated_at", "notice_date"):
            if field_name in field_names and field_name not in readonly_fields:
                readonly_fields.append(field_name)
        return readonly_fields


class CMSChangeOnlyAdmin(CMSModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CMSSingletonAdmin(CMSModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CMSNoAddAdmin(CMSModelAdmin):
    def has_add_permission(self, request):
        return False


class CMSNoDeleteAdmin(CMSModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


def image_preview(obj, field_name, width=80, height=60):
    image = getattr(obj, field_name, None)
    if not image:
        return "-"
    try:
        url = image.url
    except Exception:
        return "-"
    return format_html(
        '<img src="{}" width="{}" height="{}" style="object-fit:cover;border-radius:4px;" />',
        url,
        width,
        height,
    )


def text_excerpt(value, length=60):
    if not value:
        return "-"
    text = str(value)
    if len(text) <= length:
        return text
    return text[: max(0, length - 3)] + "..."
