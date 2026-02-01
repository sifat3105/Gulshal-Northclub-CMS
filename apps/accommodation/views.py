from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions
)

from .serializers import (
    AccommodationHeroSerializer,
    GalleryImageSerializer,
    BannerImageSerializer,
    LuxurySerializer,
    ProvideSerializer,
    ImpressionsImagesSerializer,
    ImpressionsSerializer
)


# GET ONLY + Standard Response Format

class AccommodationHeroAPI(APIView):
    def get(self, request):
        data = AccommodationHero.objects.all()
        serializer = AccommodationHeroSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Accommodation hero data fetched successfully',
            'data': serializer.data
        })


class GalleryImageAPI(APIView):
    def get(self, request):
        data = GalleryImage.objects.all()
        serializer = GalleryImageSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Gallery images fetched successfully',
            'data': serializer.data
        })


class BannerImageAPI(APIView):
    def get(self, request):
        data = BannerImage.objects.all()
        serializer = BannerImageSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Banner images fetched successfully',
            'data': serializer.data
        })


class LuxuryAPI(APIView):
    def get(self, request):
        data = Luxury.objects.all()
        serializer = LuxurySerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Luxury items fetched successfully',
            'data': serializer.data
        })


class ProvideAPI(APIView):
    def get(self, request):
        data = Provide.objects.all()
        serializer = ProvideSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Service list fetched successfully',
            'data': serializer.data
        })


class ImpressionsImagesAPI(APIView):
    def get(self, request):
        data = ImpressionsImages.objects.all()
        serializer = ImpressionsImagesSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Below impressions fetched successfully',
            'data': serializer.data
        })


class ImpressionsAPI(APIView):
    def get(self, request):
        data = Impressions.objects.all()
        serializer = ImpressionsSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Impressions fetched successfully',
            'data': serializer.data
        })
