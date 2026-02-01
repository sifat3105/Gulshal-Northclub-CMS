from django.urls import path
from .views import (
    Healthcare_gymAPIView,
    SalonAPIView,
    LoungesPartyAPIView,
    SwimmingPoolAPIView,
    BilliardSmokingAPIView,
    LibraryAPIView,
    BeautyParlorAPIView,
    LaundryAPIView,
    CardRoomAPIView,
    BanquetHallAPIView,
)

urlpatterns = [
    path("healthcare/gym/", Healthcare_gymAPIView.as_view()),
    
    path("salon/", SalonAPIView.as_view()),

    path("lounges/party/", LoungesPartyAPIView.as_view()),

    path("swimming/pool/", SwimmingPoolAPIView.as_view()),

    path("billiard-smoking/", BilliardSmokingAPIView.as_view()),

    path("library/", LibraryAPIView.as_view()),

    path("beauty-parlor/", BeautyParlorAPIView.as_view()),

    path("laundry/", LaundryAPIView.as_view()),

    path("card-room/", CardRoomAPIView.as_view()),

    path("banquet-hall/", BanquetHallAPIView.as_view()),
]
