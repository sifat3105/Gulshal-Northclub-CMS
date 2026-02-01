from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FooterBrand, UsefulLink, SocialMedia, ContactInfo, FooterCopyright
from .serializers import (
    FooterBrandSerializer, UsefulLinkSerializer, SocialMediaSerializer,
    ContactInfoSerializer, FooterCopyrightSerializer
)

class FooterFullDataView(APIView):
    def get(self, request):
        try:
            # Brand
            brand = FooterBrand.objects.first()
            brand_data = FooterBrandSerializer(brand).data if brand else None

            # Useful Links
            useful_links = UsefulLink.objects.all()
            useful_links_data = UsefulLinkSerializer(useful_links, many=True).data

            # Social Media
            social_media = SocialMedia.objects.all()
            social_media_data = SocialMediaSerializer(social_media, many=True).data

            # Contact
            contact = ContactInfo.objects.first()
            contact_data = ContactInfoSerializer(contact).data if contact else None

            # Copyright
            copyright_obj = FooterCopyright.objects.first()
            copyright_data = FooterCopyrightSerializer(copyright_obj).data if copyright_obj else None

            return Response({
                'status': 'success',
                'message': 'Footer data fetched successfully',
                'status_code': status.HTTP_200_OK,
                'data': {
                    'brand': brand_data,
                    'useful_links': useful_links_data,
                    'social_media': social_media_data,
                    'contact': contact_data,
                    'copyright': copyright_data,
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # error return
            return Response({
                'status': 'error',
                'message': 'Footer data fetch করার সময় সমস্যা হয়েছে।',
                'error': str(e),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
