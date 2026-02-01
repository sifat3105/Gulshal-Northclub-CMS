from django.db import models

# Create your models here.


class NoticeCard(models.Model):
    notice_name =models.CharField(max_length=100)
    notice_date = models.DateField(auto_now_add=True)
    notice_subject = models.CharField(max_length=255)
    notice_detail = models.TextField()
    def __str__(self):
        return self.notice_name
    