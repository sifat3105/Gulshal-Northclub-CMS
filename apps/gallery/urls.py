from django.urls import path
from .views import (
    MembershipGalleryAPIView,
    ReservationGalleryAPIView,
    MenuGalleryAPIView,
    # ===== FINE DINING =====
    MembershipFineDiningAPIView,
    ReservationFineDiningAPIView,
    MenuFineDiningAPIView,

    # ===== FINE DINING =====
    MembershipLiveMusicAPIView,
    ReservationLiveMusicAPIView,
    MenuLiveMusicAPIView,
    # ===== FINE DINING SECOND =====
    MembershipFineDiningSecondAPIView,
    ReservationFineDiningSecondAPIView,
    MenuFineDiningSecondAPIView
)

urlpatterns = [
    path("memberships/", MembershipGalleryAPIView.as_view()),
    path("reservation/", ReservationGalleryAPIView.as_view()),
    path("menu/", MenuGalleryAPIView.as_view()),

    # ===== FINE DINING =====
    path("memberships/fine-dining/",MembershipFineDiningAPIView.as_view()),
    path("reservation/fine-dining/",ReservationFineDiningAPIView.as_view()),
    path("menu/fine-dining/",MenuFineDiningAPIView.as_view()),

    # ===== FINE DINING =====
    path("memberships/live-music/",MembershipLiveMusicAPIView.as_view()),
    path("reservation/live-music/",ReservationLiveMusicAPIView.as_view()),
    path("menu/live-music/",MenuLiveMusicAPIView.as_view()),

    # ===== FINE DINING SECOND =====
    path("memberships/fine-dining-second/",MembershipFineDiningSecondAPIView.as_view()),
    path("reservation/fine-dining-second/",ReservationFineDiningSecondAPIView.as_view()),
    path("menu/fine-dining-second/",MenuFineDiningSecondAPIView.as_view()),
]
