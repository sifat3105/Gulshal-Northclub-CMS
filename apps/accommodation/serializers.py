from rest_framework import serializers
from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions
)

# Accommodation Hero Serializer
class AccommodationHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationHero
        fields = '__all__'


# Gallery Image Serializer
class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'


# Banner Image Serializer
class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = '__all__'


# Luxury Serializer
class LuxurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luxury
        fields = '__all__'


# Provide (We Provide Section) Serializer
class ProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provide
        fields = '__all__'


# Below Impressions Serializer
class ImpressionsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpressionsImages
        fields = '__all__'


# Main Impressions Serializer
class ImpressionsSerializer(serializers.ModelSerializer):
    impressions_image = ImpressionsImagesSerializer(read_only=True)

    class Meta:
        model = Impressions
        fields = '__all__'

