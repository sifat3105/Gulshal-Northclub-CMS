from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions,
    Suite,
    SuiteImage,
)

from .serializers import (
    AccommodationHeroSerializer,
    GalleryImageSerializer,
    BannerImageSerializer,
    LuxurySerializer,
    ProvideSerializer,
    ImpressionsImagesSerializer,
    ImpressionsSerializer,
    SuiteImageSerializer,
    SuiteListSerializer,
    SuiteDetailSerializer,
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


class SuiteListView(APIView):
    
    def get(self, request):
        suites = Suite.objects.filter(is_active=True)
        serializer = SuiteListSerializer(suites, many=True, context={'request': request})
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Suites fetched successfully',
            'data': serializer.data
        })
        
class SuiteDetailView(APIView):
    
    def get(self, request, slug):
        suite = get_object_or_404(Suite.objects.prefetch_related('images'), slug=slug, is_active=True)
        serializer = SuiteDetailSerializer(suite, context={'request': request})
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Suite details fetched successfully',
            'data': serializer.data
        })