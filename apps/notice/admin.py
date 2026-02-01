from django.contrib import admin
from .models import NoticeCard


# Register your models here.

@admin.register(NoticeCard)
class NoticeCardAdmin(admin.ModelAdmin):
    list_display = ('notice_name', 'notice_subject', 'notice_date')
    search_fields = ('notice_name', 'notice_subject')
    list_filter = ('notice_date',)

