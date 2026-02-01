from django.urls import path
from .views import (
    RunningEventAPIView,
    UpcomingEventAPIView,
    PastEventAPIView,
    PastEventPhotoAPIView,
    CompletedEventAPIView,
    FineDiningAPIView,
    LiveMusicAPIView,
    FineDiningSecondAPIView,
    EventGalleryAPIView,

    RunningEventHeroAPIView,
    UpcomingEventHeroAPIView,
    PastEventHeroAPIView,
)


urlpatterns = [
    path("running/event/hero/", RunningEventHeroAPIView.as_view()),
    path("upcoming/event/hero/", UpcomingEventHeroAPIView.as_view()),
    path("past/event/hero/", PastEventHeroAPIView.as_view()),


    path("running/", RunningEventAPIView.as_view()),
    path("upcoming/", UpcomingEventAPIView.as_view()),
    path("past/", PastEventAPIView.as_view()),
    path("past/photo/", PastEventPhotoAPIView.as_view()),

    path("completed/", CompletedEventAPIView.as_view()),

    path("fine-dining/", FineDiningAPIView.as_view()),
    path("live-music/", LiveMusicAPIView.as_view()),
    path("fine-dining-2/", FineDiningSecondAPIView.as_view()),

    path("gallery/", EventGalleryAPIView.as_view()),
]