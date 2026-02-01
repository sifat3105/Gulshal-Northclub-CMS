from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceDetailSerializer

# Create your views here.


class BasePlaceAPIView(APIView):
    place_type = None

    def get(self, request):
        place = Place.objects.filter(place_type=self.place_type).first()

        if not place:
            return Response(
                {"message": "Data not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PlaceDetailSerializer(place)

        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            "section": self.place_type,
            'message': 'facilities data fetched successfully',
            'data': serializer.data
        })

class Healthcare_gymAPIView(BasePlaceAPIView):
    place_type = "healthcare_gym"

class SalonAPIView(BasePlaceAPIView):
    place_type = "salon"

class LoungesPartyAPIView(BasePlaceAPIView):
    place_type = "lounges_party"

class SwimmingPoolAPIView(BasePlaceAPIView):
    place_type = "swimming_pool"


class BilliardSmokingAPIView(BasePlaceAPIView):
    place_type = "billiard_smoking"


class LibraryAPIView(BasePlaceAPIView):
    place_type = "library"


class BeautyParlorAPIView(BasePlaceAPIView):
    place_type = "beauty_parlor"


class LaundryAPIView(BasePlaceAPIView):
    place_type = "laundry"


class CardRoomAPIView(BasePlaceAPIView):
    place_type = "card_room"


class BanquetHallAPIView(BasePlaceAPIView):
    place_type = "banquet_hall"
