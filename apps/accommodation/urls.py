from django.urls import path
from .views import (
    AccommodationHeroAPI,
    GalleryImageAPI,
    BannerImageAPI,
    LuxuryAPI,
    ProvideAPI,
    ImpressionsImagesAPI,
    ImpressionsAPI
)

urlpatterns = [
    path('hero/', AccommodationHeroAPI.as_view()),
    path('gallery/', GalleryImageAPI.as_view()),
    path('banner/', BannerImageAPI.as_view()),
    path('luxury/', LuxuryAPI.as_view()),
    path('provide/', ProvideAPI.as_view()),
    path('below-impressions/', ImpressionsImagesAPI.as_view()),
    path('impressions/', ImpressionsAPI.as_view()),
]

