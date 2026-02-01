from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Gallery,GallerySection
from .serializers import GallerySerializer ,GallerySectionSerializer


class BaseGalleryAPIView(APIView):
    gallery_type = None

    def get_queryset(self):
        if not self.gallery_type:
            return Gallery.objects.none()

        return (
            Gallery.objects
            .filter(
                gallery_type=self.gallery_type,
                is_active=True
            )
            .prefetch_related("images")
            .order_by("-created_at")
        )

    def get(self, request):
        queryset = self.get_queryset()
        serializer = GallerySerializer(queryset, many=True)

        return Response(
            {
                "status": "success",
                "section": self.gallery_type,
                "count": queryset.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )


class MembershipGalleryAPIView(BaseGalleryAPIView):
    gallery_type = "memberships"


class ReservationGalleryAPIView(BaseGalleryAPIView):
    gallery_type = "reservation"


class MenuGalleryAPIView(BaseGalleryAPIView):
    gallery_type = "menu"



class BaseSectionAPIView(APIView):
    page = None
    section_type = None

    def get(self, request):
        queryset = (
            GallerySection.objects
            .filter(
                page=self.page,
                section_type=self.section_type,
                is_active=True
            )
            .prefetch_related("images")
            .order_by("id")
        )

        if not queryset.exists():
            return Response(
                {
                    "status": "error",
                    "message": "Data not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GallerySectionSerializer(queryset, many=True)

        return Response(
            {
                "status": "success",
                "page": self.page,
                "section": self.section_type,
                "count": queryset.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )

# FINE DINING APIs
class MembershipFineDiningAPIView(BaseSectionAPIView):
    page = "memberships"
    section_type = "fine_dining"


class ReservationFineDiningAPIView(BaseSectionAPIView):
    page = "reservation"
    section_type = "fine_dining"


class MenuFineDiningAPIView(BaseSectionAPIView):
    page = "menu"
    section_type = "fine_dining"


# LIVE MUSIC APIs
class MembershipLiveMusicAPIView(BaseSectionAPIView):
    page = "memberships"
    section_type = "live_music"


class ReservationLiveMusicAPIView(BaseSectionAPIView):
    page = "reservation"
    section_type = "live_music"


class MenuLiveMusicAPIView(BaseSectionAPIView):
    page = "menu"
    section_type = "live_music"

# FINE DINING (SECOND) APIs
class MembershipFineDiningSecondAPIView(BaseSectionAPIView):
    page = "memberships"
    section_type = "fine_dining_2"


class ReservationFineDiningSecondAPIView(BaseSectionAPIView):
    page = "reservation"
    section_type = "fine_dining_2"


class MenuFineDiningSecondAPIView(BaseSectionAPIView):
    page = "menu"
    section_type = "fine_dining_2"
