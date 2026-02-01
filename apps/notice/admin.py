from django.contrib import admin
from .models import NoticeCard
from project.admin_helpers import CMSModelAdmin, text_excerpt


@admin.register(NoticeCard)
class NoticeCardAdmin(CMSModelAdmin):
    list_display = ("notice_name", "notice_subject", "detail_preview", "notice_date")
    search_fields = ("notice_name", "notice_subject", "notice_detail")
    list_filter = ("notice_date",)
    date_hierarchy = "notice_date"
    ordering = ("-notice_date",)

    @admin.display(description="Detail")
    def detail_preview(self, obj):
        return text_excerpt(obj.notice_detail, length=90)
