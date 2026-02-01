from django.urls import path
from .views import (
    AboutHeroListAPIView,
    TopgalleryListAPIView,
    BottomgalleryListAPIView,
    AboutForHeritageListAPIView,
    MemberTypeListAPIView,
    BoardMemberListAPIView,
    DetilImagesAPIView,
    SocialMediaLinkListAPIView,
    PresidentAPIView,
)

urlpatterns = [
    # About Section
    path('about-hero/', AboutHeroListAPIView.as_view(), name='about-hero'),
    path('top-gallery/', TopgalleryListAPIView.as_view(), name='top-gallery'),
    path('bottom-gallery/', BottomgalleryListAPIView.as_view(), name='bottom-gallery'),
    path('heritage/', AboutForHeritageListAPIView.as_view(), name='heritage'),

    # Member Section
    path('member-types/', MemberTypeListAPIView.as_view(), name='member-types'),
    path('board-members/', BoardMemberListAPIView.as_view(), name='board-members'),
    
    path('gncl/president/', PresidentAPIView.as_view(), name='president-gncl'),
    
    path('social-links/', SocialMediaLinkListAPIView.as_view(), name='social-links'),
    path('detail-image/', DetilImagesAPIView.as_view(), name='detail-image'),
]
