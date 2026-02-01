from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.db.models import QuerySet

from .models import NoticeCard
from .serializers import NoticeCardSerializers


# Pagination
class NoticePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "status": "success",
            "status_code": status.HTTP_200_OK,
            "message": "Notices fetched successfully",

            # Data first
            "data": data,

            # Pagination after data
            "pagination": {
                "total_items": self.page.paginator.count,
                "page": self.page.number,
                "page_size": self.page.paginator.per_page,
                "total_pages": self.page.paginator.num_pages,
                "has_next": self.page.has_next(),
                "has_previous": self.page.has_previous(),
                "next_page": self.page.next_page_number() if self.page.has_next() else None,
                "previous_page": self.page.previous_page_number() if self.page.has_previous() else None,
            }
        })


# Advanced List API (Search + Filter + Pagination)
class NoticeListView(generics.ListAPIView):
    serializer_class = NoticeCardSerializers
    pagination_class = NoticePagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ["notice_name", "notice_subject", "notice_date"]
    search_fields = ["notice_name", "notice_subject"]
    ordering_fields = ["notice_date", "notice_name"]
    ordering = ["-notice_date"]

    def get_queryset(self) -> QuerySet:
        return NoticeCard.objects.all().order_by("-notice_date")


# Simple List API (Pagination Only)
class NoticeCaredAPIView(APIView):
    def get(self, request):
        try:
            queryset = NoticeCard.objects.all().order_by("-notice_date")

            paginator = NoticePagination()
            page = paginator.paginate_queryset(queryset, request)

            if page is None:
                return Response({
                    "status": "success",
                    "status_code": status.HTTP_200_OK,
                    "message": "No data available",
                    "data": [],
                    "pagination": None
                })

            serializer = NoticeCardSerializers(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        except Exception as e:
            # Production-safe error response
            return Response({
                "status": "error",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Something went wrong",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
