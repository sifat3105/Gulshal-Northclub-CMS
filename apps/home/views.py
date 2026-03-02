from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *

from apps.about.models import BoardMember
from apps.about.serializers import BoardMemberSerializerForHome


# Hero List API
class HeroListAPIView(APIView):
    def get(self, request):
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'get data successfully',
            'data': serializer.data
        })


# Club Facilities Head API 
class ClubFacilitiesHeadAPIView(APIView):
    def get(self, request):
        obj, _ = ClubFacilitiesHead.objects.get_or_create(id=1)
        serializer = ClubFacilitiesHeadSerializer(obj)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Facilities List API
class FacilitiesAPIView(APIView):
    def get(self, request):
        items = Facilities.objects.all()
        serializer = FacilitiesSerializer(items, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Our Moments Head API
class OurMomentsHeadAPIView(APIView):
    def get(self, request):
        obj, _ = OurMomentsHead.objects.get_or_create(id=1)
        serializer = OurMomentsHeadSerializer(obj)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Our Moments Images API
class OurMomentsAPIView(APIView):
    def get(self, request):
        data = OurMoments.objects.all()
        serializer = OurMomentsSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Affiliations / Collaborations Head API
class AffiliatCollabHeadAPIView(APIView):
    def get(self, request):
        obj, _ = AffiliatCollabHead.objects.get_or_create(id=1)
        serializer = AffiliatCollabHeadSerializer(obj)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Affiliations / Collaborations Logos API
class AffiliatCollabAPIView(APIView):
    def get(self, request):
        data = AffiliatCollab.objects.all()
        serializer = AffiliatCollabSerializer(data, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Club Events Head API
class ClubEventHeadAPIView(APIView):
    def get(self, request):
        obj, _ = ClubEventHead.objects.get_or_create(id=1)
        serializer = ClubEventHeadSerializer(obj)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })


# Club Events List API
class ClubEventsAPIView(APIView):
    def get(self, request):
        events = ClubEvents.objects.all()
        serializer = ClubEventsSerializer(events, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })



#Board of directors

class BoardOfDirectorsAPIView(APIView):
    def get(self, request):
        members = BoardMember.objects.all()
        serializer = BoardMemberSerializerForHome(members, many=True)
        return Response({
            'status': 'success',
            'status_code': status.HTTP_200_OK,
            'message': 'Data fetched successfully',
            'data': serializer.data
        })
        
