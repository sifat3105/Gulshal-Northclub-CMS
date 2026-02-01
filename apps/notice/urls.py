from django.urls import path
from .views import NoticeListView, NoticeCaredAPIView

urlpatterns = [
    path("notices/all/", NoticeCaredAPIView.as_view(), name="notice-all"),
    path("card/list/", NoticeListView.as_view(), name="notice-list"),
]
