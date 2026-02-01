from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# ---------------- About Section ----------------
class AboutHeroListAPIView(APIView):
    def get(self, request):
        items = AboutHero.objects.all()
        serializer = AboutHeroSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'About Hero list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class TopgalleryListAPIView(APIView):
    def get(self, request):
        items = Topgallery.objects.all()
        serializer = TopgallerySerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Top gallery list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class BottomgalleryListAPIView(APIView):
    def get(self, request):
        items = Bottomgallery.objects.all()
        serializer = BottomgallerySerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Bottom gallery list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class AboutForHeritageListAPIView(APIView):
    def get(self, request):
        items = AboutForHeritage.objects.all()
        serializer = AboutForHeritageSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Heritage list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })




class PresidentAPIView(APIView):

    def get(self, request):
        item = President.objects.first()

        if not item:
            return Response({
                'status': 'error',
                'message': 'No president data found',
                'status_code': status.HTTP_404_NOT_FOUND,
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutPresidentSerializer(item)
        return Response({
            'status': 'success',
            'message': 'President data fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class MemberTypeListAPIView(APIView):
    def get(self, request):
        items = MemberType.objects.all()
        serializer = MemberTypeSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Member types list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class BoardMemberListAPIView(APIView):
    def get(self, request):
        items = BoardMember.objects.all()
        serializer = BoardMemberSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Board members list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })


class DetilImagesAPIView(APIView):
    def get(self, request):
        items = DetailImage.objects.all()
        serializer = DetailImageSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Social media links list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })
    
class SocialMediaLinkListAPIView(APIView):
    def get(self, request):
        items = SocialMediaLink.objects.all()
        serializer = SocialMediaLinkSerializer(items, many=True)
        return Response({
            'status': 'success',
            'message': 'Social media links list fetched successfully',
            'status_code': status.HTTP_200_OK,
            'data': serializer.data
        })
