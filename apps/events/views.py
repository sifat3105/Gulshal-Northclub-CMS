from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Event,EventHero
from .serializers import EventSerializer,EventHeroSerializer



class BaseEventHeroAPIView(APIView):
    event_type = None

    def get(self, request):
        hero = (
            EventHero.objects
            .filter(
                event_type=self.event_type,
                is_active=True
            )
            .order_by("-created_at")
            .first()
        )

        if not hero:
            return Response(
                {"message": "Hero not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EventHeroSerializer(hero)
        return Response(
            {
                "status": "success",
                "event_type": self.event_type,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )


class RunningEventHeroAPIView(BaseEventHeroAPIView):
    event_type = "running"


class UpcomingEventHeroAPIView(BaseEventHeroAPIView):
    event_type = "upcoming"


class PastEventHeroAPIView(BaseEventHeroAPIView):
    event_type = "past"



class BaseEventAPIView(APIView):

    event_type = None

    def get_queryset(self):
        if not self.event_type:
            return Event.objects.none()

        return (
            Event.objects
            .filter(
                event_type=self.event_type,
                is_active=True
            )
            .prefetch_related("images")
            .order_by("-created_at")
        )

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)

        return Response(
            {
                "status": "success",
                "section": self.event_type,
                'message': 'Event data fetched successfully',
                "count": queryset.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )


# ===== EVENT STATUS APIs =====
class RunningEventAPIView(BaseEventAPIView):
    event_type = "running"


class UpcomingEventAPIView(BaseEventAPIView):
    event_type = "upcoming"

class PastEventAPIView(BaseEventAPIView):
    event_type = "past"

class PastEventPhotoAPIView(BaseEventAPIView):
    event_type = "past_photo"


class CompletedEventAPIView(BaseEventAPIView):
    event_type = "completed"


# ===== EXPERIENCE SECTION APIs =====
class FineDiningAPIView(BaseEventAPIView):
    event_type = "fine_dining"


class LiveMusicAPIView(BaseEventAPIView):
    event_type = "live_music"


class FineDiningSecondAPIView(BaseEventAPIView):
    event_type = "fine_dining_2"


# ===== GALLERY API =====
class EventGalleryAPIView(BaseEventAPIView):
    event_type = "gallery"
