from django.urls import path
from .views import *
from app.events.views import EventGalleryAPIView

urlpatterns = [
    path('hero/', HeroListAPIView.as_view()), 

    path('club-facilities-head/', ClubFacilitiesHeadAPIView.as_view()),
    path('facilities/', FacilitiesAPIView.as_view()),

    path('our-moments-head/', OurMomentsHeadAPIView.as_view()),
    path('our-moments/', EventGalleryAPIView.as_view()),  #chaned url as maruf vai requested

    path('affiliat-collab-head/', AffiliatCollabHeadAPIView.as_view()),
    path('affiliat-collab/', AffiliatCollabAPIView.as_view()),

    path('club-event-head/', ClubEventHeadAPIView.as_view()),
    path('club-events/', ClubEventsAPIView.as_view()),
    path('board-of-directors/', BoardOfDirectorsAPIView.as_view()),
]
